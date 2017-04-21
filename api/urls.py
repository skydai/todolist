from django.conf.urls import patterns, include, url

from api.views import TaskList, TaskDetail

urlpatterns = patterns('',

    url(r'^tasks/$', TaskList.as_view(), name = 'list' ),
    url(r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name = 'detail' ),
)