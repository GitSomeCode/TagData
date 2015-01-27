from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponseForbidden
from main import *
from tags.models import Tag, TagRelation
from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.
class DisplayRelations(ListView):
  model = Tag
  template_name = "tags/relations.html"
  #paginate_by = 50
  #page_kwarg = "page"

  def get_queryset(self):
    searched_tag = self.request.GET.get("s", None)
    if not searched_tag:
      return None
    root_tag = get_object_or_404(Tag, name=searched_tag)
    
    '''
    Compiling all relations to searched tag.
    Uses getRelation method from main.py because searched tag may be in a relation where it is either a tag_to or tag_from.
    Also gets metric between the two tags.
    Information for each relation is stored in a tuple.
    Stores all relations in relations_list.
    Ex. relations to 'rock' -- [('indie', 0.8793), ('pop', 1.342), ..., (related_tag, metric)]
    '''
    def relationsList(search):
      mylist = []
      for tag in Tag.objects.all():
        relation = getRelation(search, tag.name)
        if relation:
          t = ()
          if relation.tag_to.name == search:
            print relation.tag_from.name
            print relation.metric
            t += (relation.tag_from.name, relation.metric)
            mylist.append(t)
          else:
            print relation.tag_to.name
            print relation.metric
            t += (relation.tag_to.name, relation.metric)
            mylist.append(t)
      return mylist

    return relationsList(searched_tag)
  
  def get_context_data2(self, **kwargs):
    pass
  
    
    