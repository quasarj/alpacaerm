from django.conf.urls import patterns, include, url

urlpatterns = patterns('vendor.views',
    url(r'^$', 'index', name='vendor'),

    url(r'^add/$', 'add', name='vendor_add'),
    url(r'^view/$', 'view_all', name='vendor_view'),

    url(r'^search/$', 'search', name='vendor_search'),
    url(r'^search_name/$', 'search_name', name='vendor_search_name'),
    url(r'^search_class/$', 'search_class', name='vendor_search_class'),
    url(r'^search_pending/$', 'search_pending', name='vendor_search_pending'),

    url(r'^item/(?P<vendor_id>\d+)/$', 'view_item', name='vendor_item'),
)
