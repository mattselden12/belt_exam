from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^travels/$', views.travels),
    url(r'^addtrip/$', views.addtrip),
    url(r'^view/(?P<idnumber>\d+)/$', views.viewplan),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^create/$', views.create),
    url(r'^join/(?P<idnumber>\d+)/$', views.join),
    url(r'^cancel/(?P<idnumber>\d+)/$', views.cancel),
    url(r'^delete/(?P<idnumber>\d+)/$', views.delete),
]