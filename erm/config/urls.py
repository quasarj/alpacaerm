from django.conf.urls import patterns, include, url

urlpatterns = patterns('config.views',
    url(r'^$', 'index', name="config"),
    url(r'^user/$', 'user', name="config_user"),
    url(r'^erm/$', 'index', name="config_erm"),
    url(r'^dashboard/$', 'index', name="config_dashboard"),
    # url(r'^(?P<poll_id>\d+)/$', 'detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
