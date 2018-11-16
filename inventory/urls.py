from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^vendor/(?P<pk>\d+)/$', views.vendor_detail, name='vendor_detail'),
    url(r'^vendor/new/$', views.vendor_new, name='vendor_new'),
    url(r'^vendor/(?P<pk>\d+)/edit/$', views.vendor_edit, name='vendor_edit'),
    ]
