from django.conf.urls import patterns, include, url

from todo.views import Home

urlpatterns = patterns('',
                       url(r'^api/', include('api.urls')),
                       url(r'^$', Home.as_view()),
                       )
