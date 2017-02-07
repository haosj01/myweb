__author__ = 'haosj'

from django.conf.urls import url
from learn import views_if,views_if_sec

urlpatterns=[
    url(r'^add_event/',views_if.add_event,name='add_event'),
    url(r'^get_event_list/',views_if.get_event_list,name='get_event_list'),
    url(r'^sec_get_event_list/',views_if.get_event_list,name='get_event_list'),
    ]