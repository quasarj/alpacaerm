from django.conf.urls import patterns, include, url


urlpatterns = patterns('erm.views',
    url(r'^$', 'index', name='erm'),
    url(r'^login/$', 'login_page', name='login'),
    url(r'^login_process/$', 'login_process', name='login_process'),
    url(r'^logout/$', 'logout_view', name='logout'),
    url(r'^risk/(?P<bankrisk_id>\d+)/$', 'bankrisk_view', name='risk'),
    # url(r'^assign/$', 'assign_view', name='assign'),
    url(r'^add/$', 'add_view', name='add'),
    url(r'^delete/(?P<bankrisk_id>\d+)/$', 'delete_view', name='erm_delete'),
    url(r'^all/$', 'all_view', name='all'),

    url(r'^search/$', 'search_view', name='search'),
    url(r'^search/source/$', 'search_bysource_view', name='search_source'),
    url(r'^search/type/$', 'search_bytype_view', name='search_type'),
    url(r'^search/date/$', 'search_bydate_view', name='search_date'),
    url(r'^search/name/$', 'search_byname_view', name='search_name'),

    url(r'^report/$', 'report_view', name='report'),
    url(r'^report_edit_text/$', 'report_edit_text', name='report_edit_text'),


    url(r'^banksetup/$', 'banksetup_view', name='erm_banksetup'),


)
