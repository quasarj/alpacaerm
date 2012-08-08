from django.conf.urls import patterns, include, url

urlpatterns = patterns('home.views',
    url(r'^$', 'index', name="home"),
    url(r'^chartdata/(?P<chart_id>\d+)/$', 'chart_data', name='home_chartdata'),
    # url(r'^(?P<poll_id>\d+)/$', 'detail'),
    # url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
