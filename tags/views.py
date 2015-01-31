from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponseForbidden
from main import *
from tags.models import Tag, TagRelation
from django.views.generic import DetailView, ListView, TemplateView, View
from operator import itemgetter
import json

# small view for Error 404 page
def error404(request):
    return render(request, 'tags/404.html')


class DisplayRelations(ListView):
  model = Tag
  template_name = "tags/relations.html"
  paginate_by = 50
  page_kwarg = "page"
  
  def get_context_data(self, **kwargs):
    context = super(DisplayRelations, self).get_context_data(**kwargs)
    context['searched'] = self.request.GET.get('s', None)
    return context

  def get_queryset(self):
    searched_tag = self.request.GET.get("s", None)
    if not searched_tag:
      raise Http404
    root_tag = get_object_or_404(Tag, name=searched_tag)
    
    '''
    Compiling all relations to searched tag.
    Ex. relations to 'rock' -- [('indie', 0.8793), ('pop', 1.342), ..., (related_tag, metric)]
    '''
    
    def relationsList(search):
      mylist = []
      tagtolist = []
      tagfromlist = []

      # TAG TO == search 

      #returns a list of tag relations ordered by closest association
      tagtolist = search.tag_to.all().order_by("metric").reverse()
      for r in tagtolist:
        t = ()
        t += (r.tag_from.name, r.metric)
        mylist.append(t)



      # TAG FROM == search 

      #returns a list of tag relations ordered by closest association
      tagfromlist = search.tag_from.all().order_by("metric").reverse()
      
      for r in tagfromlist:
        t = ()
        t += (r.tag_to.name, r.metric)
        mylist.append(t)
     
      ### mylist has all of rock's relations, need to order them by metric
      ### which is second tuple 

      sorted(mylist, key=lambda x: x[1], reverse=True)
      
      return mylist
    
    query_set = relationsList(root_tag)
    return query_set

class CompareLastFM(View):
  '''
  Sends JSON data -- top 50 of our similar tags, and top 50 of last.fm's similar tags
  '''
  def get(self, request, *args, **kwargs):
    tag_to_compare = self.request.GET.get("s", None)
    lastfmResults = {"tagbits":self.getMostSimilar(tag_to_compare), "lastfm": compareLastFM(tag_to_compare)}
    return HttpResponse(json.dumps(lastfmResults), content_type="application/json")
  
  '''
  Compiles a list of similar tags to original search.
  Used for compare option.
  '''
  def getMostSimilar(self, compare):
    relations_names = []
    
    # name is passed, but we need Tag
    compare_tag = Tag.objects.get(name=compare)
    
    # returns a list of tag relations ordered by closest association
    relations_list= compare_tag.tag_to.all().order_by("metric").reverse()
    
    for r in relations_list:
        if r.tag_to.name == compare:
            relations_names.append(r.tag_from.name)
        else:
            relations_names.append(r.tag_to.name)
            
    return relations_names[:50]
    
    
  
  
  
  
  
    
    