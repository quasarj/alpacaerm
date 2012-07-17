from django.conf.urls import patterns, include, url

urlpatterns = patterns('audit.views',
    url(r'^$', 'index', name="audit"),
    # url(r'^(?P<poll_id>\d+)/$', 'detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
