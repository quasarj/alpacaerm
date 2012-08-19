
from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from vendor.models import Vendor

# CHECKBOX_ATTRS = {'class': 'risk_checkbox'}

class VendorForm(ModelForm):

    class Meta:
        model = Vendor
        exclude = (
            'bank',
            # exclude the calculated fields
            'vendorRiskRating',
            'priorRiskRating',
            'inherentRiskRating',
        )
        # widgets = {
        #     'actionItem': forms.TextInput(attrs={'size': 60}),
        #     'recommendation': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'managementResponse': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'remediation': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'comments': Textarea(attrs={'cols': 80, 'rows': 10}),
        #     'riskSources': FilteredSelectMultiple("sources", is_stacked=False, attrs={'rows': '10'}), 
        # }

