from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^travels/$', views.travels),
    url(r'^addtrip/$', views.addtrip),
    url(r'^view/(?P<idnumber>\d+)/$', views.viewplan),
    url(r'^logout/$', views.logout),
]