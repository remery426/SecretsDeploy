from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dashboard$', views.index),
    url(r'createpost$', views.createpost),
    url(r'logout$',views.logout),
    url(r'delete/(?P<id>\d*)$', views.delete),
    url(r'like/(?P<id>\d*)$', views.like)
]
