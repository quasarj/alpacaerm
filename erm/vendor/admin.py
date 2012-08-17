from vendor.models import *
import reversion

from django.contrib import admin

class VendorAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Vendor, VendorAdmin)


# class AgencyAdmin(reversion.VersionAdmin):
#     pass

# admin.site.register(Agency)


