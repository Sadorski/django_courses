from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^delete/(?P<id>\d+)$', views.remove),
    url(r'^destroy/(?P<id>\d+)$', views.confirm), 
    url(r'^create$', views.add)    # This line has changed!
]