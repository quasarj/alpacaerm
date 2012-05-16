from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erm.views.home', name='home'),
    # url(r'^erm/', include('erm.foo.urls')),

    # Todo: See Django tutorial Part 3 for information on
    #       decoupling the URLConfs.

#    url(r'^polls/$', 'polls.views.index'),
#    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
#    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
#    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),


    url(r'^$', 'erm.views.index'),
    url(r'^erm/$', 'erm.views.index'),
    url(r'^erm/login/$', 'erm.views.login_page'),
    url(r'^erm/login_process/$', 'erm.views.login_process'),
    url(r'^erm/logout/$', 'erm.views.logout_view'),
    url(r'^erm/risk/(?P<risk_id>\d+)/$', 'erm.views.risk'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
