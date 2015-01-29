from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from tags import views

urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="tags/index.html"), name="index"),
  url(r'^tag/$', views.DisplayRelations.as_view(), name="relations"), 
  url(r'^compare/tag/$', views.CompareLastFM.as_view(), name="compare"),
  url(r'^about/$', TemplateView.as_view(template_name="tags/about.html"), name="about"),
  url(r'^contact/$', TemplateView.as_view(template_name="tags/contact.html"), name="contact"),
  #url(r'^', views.tagData, name="tagData"),                     
)