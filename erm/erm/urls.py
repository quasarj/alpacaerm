from django.conf.urls import patterns, include, url


urlpatterns = patterns('erm.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'login_page'),
    url(r'^login_process/$', 'login_process'),
    url(r'^logout/$', 'logout_view'),
    url(r'^risk/(?P<bankrisk_id>\d+)/$', 'bankrisk_view'),
    url(r'^assign/$', 'assign_view'),
    url(r'^add/$', 'add_view'),
    url(r'^all/$', 'all_view'),

    url(r'^search/$', 'search_view'),
    url(r'^search/source/$', 'search_bysource_view'),
    url(r'^search/type/$', 'search_bytype_view'),
    url(r'^search/date/$', 'search_bydate_view'),
    url(r'^search/name/$', 'search_byname_view'),

    url(r'^report/$', 'report_view'),
)
