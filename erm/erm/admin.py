from erm.models import Bank, Risk, BankRisk, RiskProfile, UserProfile, RiskType, RiskSource

from django.contrib import admin

admin.site.register(Bank)
admin.site.register(Risk)
admin.site.register(BankRisk)
admin.site.register(RiskProfile)
admin.site.register(RiskType)
admin.site.register(RiskSource)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('bank', 'user', 'level')

admin.site.register(UserProfile, UserProfileAdmin)

