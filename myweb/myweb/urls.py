"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views
from django.conf.urls import url,include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^login/$',views.login),
    url(r'^event_manage/$',views.release),
    url(r'^accounts/login/$',views.index),
    url('^sreach_name/$',views.sreach_name),
    url('^guest_manage/$',views.guest_manage),
    url('^sreach_guest/$',views.sreach_guest),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$',views.sign_index),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$',views.sign_index_action),
    url(r'^logout/$',views.logout),
    url(r'^api/',include('learn.urls',namespace="learn")),
]
