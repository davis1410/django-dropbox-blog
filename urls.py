from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list),
    url(r'^(?P<c_slug>[\w]+)/$', views.category),
    url(r'^(?P<p_slug>[\-\w]+)/$', views.post),
]