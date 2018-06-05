

from django.conf.urls import url
from django.contrib import admin
from api.view.course import CourseView
from api.view.technology import TechnologyView
from api.view.account import LoginView



urlpatterns = [

    url('^course/$',CourseView.as_view({"get":"list"})),
    url('^course/(?P<pk>\d+)/',CourseView.as_view({"get":"retrieve"})),
    url('^technology/$',TechnologyView.as_view({"get":"list"})),
    url('^technology/(?P<pk>\d+)',TechnologyView.as_view({"get":"retrieve"})),
    url('^login/$',LoginView.as_view())
]
