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
  paginate_by = 50
  page_kwarg = "page"

  def get_queryset(self):
    self.tag_search = self.request.GET.get("tag_search", None)
    if not self.tag_search:
      return None
    self.root_tag = get_object_or_404(Tag, name=tag_search)
    
    '''
    Compiling all relations to searched tag.
    Uses getRelation method from main.py because searched tag may be in a relation where it is either a tag_to or tag_from.
    Stores all relations in relations_list.
    '''
    self.relations_list = []
    self.all_Tags = Tag.objects.get()
    
    for tag.name in self.all_Tags:
      relation = getRelation(self.tag_search, tag.name)
      if relation:
        self.relations_list.append(relation)
    
    
  
  def get_context_data(self, **kwargs):
    pass
  
    
    