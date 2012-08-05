from exception.models import *
import reversion

from django.contrib import admin

class ExceptionAdmin(reversion.VersionAdmin):
    pass


admin.site.register(Exception, ExceptionAdmin)
admin.site.register(Agency)


