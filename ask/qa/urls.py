from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.test, name='question'),
    url(r'(?P<id>[0-9]+)/$', views.test, name='question'),
]
