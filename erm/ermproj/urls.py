from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # This needs to go to a special "home" page
    # that is seperate from each module/app.
    # Maybe it can be housed in the same app the
    # login stuff is in?
    url(r'^$', 'ermproj.views.home', name="home"),


    url(r'^erm/', include('erm.urls')),
    url(r'^vendor/', include('vendor.urls')),
    url(r'^exception/', include('exception.urls')),
    url(r'^audit/', include('audit.urls')),

    # special url for logging in
    # TODO: This should be it's own app, I think.
    url(r'^accounts/login/$', 'erm.views.login_page', name="autologin"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
