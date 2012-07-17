from django.conf.urls import patterns, include, url

urlpatterns = patterns('exception.views',
    url(r'^$', 'index', name="exception"),
    # url(r'^(?P<poll_id>\d+)/$', 'detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
