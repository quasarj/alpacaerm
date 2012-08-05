from exception.models import *
import reversion

from django.contrib import admin

class ExceptionAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Exception, ExceptionAdmin)


class AgencyAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Agency)


