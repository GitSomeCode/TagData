from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from tags import views

urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="tags/index.html"), name="index"),
  url(r'^tag/$', views.DisplayRelations.as_view(), name="relations"), 
  #url(r'^', views.tagData, name="tagData"),                     
)