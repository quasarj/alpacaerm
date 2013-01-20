from django.conf.urls import patterns, include, url

urlpatterns = patterns('exception.views',
    url(r'^$', 'index', name="exception"),

    url(r'^add/$', 'add', name='exception_add'),
    url(r'^open/$', 'view_open', name='exception_open'),
    url(r'^closed/$', 'view_closed', name='exception_closed'),

    url(r'^search/$', 'search_main', name='exception_search'),
    url(r'^search/date/$', 'search_date', name='exception_search_date'),
    url(r'^search/action/$', 'search_action', name='exception_search_action'),
    url(r'^search/agency/$', 'search_agency', name='exception_search_agency'),

    url(r'^item/(?P<exception_id>\d+)/$', 'view_item', name='exception_item'),
    url(r'^delete/(?P<exception_id>\d+)/$', 'delete', name='exception_delete'),
)
