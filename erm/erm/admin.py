from erm.models import Bank, Risk, BankRisk, RiskProfile, UserProfile

from django.contrib import admin

admin.site.register(Bank)
admin.site.register(Risk)
admin.site.register(BankRisk)
admin.site.register(RiskProfile)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('bank', 'user', 'level')

admin.site.register(UserProfile, UserProfileAdmin)

