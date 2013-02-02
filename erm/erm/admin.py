from erm.models import *
import reversion

from django.contrib import admin


admin.site.register(Bank)



class BankRiskAdmin(reversion.VersionAdmin):
    pass
admin.site.register(BankRisk, BankRiskAdmin)


class RiskTypeAdmin(reversion.VersionAdmin):
    pass
admin.site.register(RiskType, RiskTypeAdmin)


class RiskSourceAdmin(reversion.VersionAdmin):
    pass
admin.site.register(RiskSource, RiskSourceAdmin)


class RiskManagerAdmin(reversion.VersionAdmin):
    pass
admin.site.register(RiskManager, RiskManagerAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('bank', 'user', 'level')
admin.site.register(UserProfile, UserProfileAdmin)

