# ModelForms go here

from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from exception.models import Exception

CHECKBOX_ATTRS = {'class': 'risk_checkbox'}
RISK_ATTRS = {'class': 'risk_risk', 'size': 4}
WEIGHT_ATTRS = {'class': 'risk_weight', 'size': 4}

class ExceptionForm(ModelForm):

    class Meta:
        model = Exception
        exclude = ('bank', 'compositeRiskScore')
        widgets = {
            'actionItem': forms.TextInput(attrs={'size': 60}),
            'recommendation': Textarea(attrs={'cols': 80, 'rows': 10}),
            'managementResponse': Textarea(attrs={'cols': 80, 'rows': 10}),
            'remediation': Textarea(attrs={'cols': 80, 'rows': 10}),
            'comments': Textarea(attrs={'cols': 80, 'rows': 10}),
            'riskSources': FilteredSelectMultiple("sources", is_stacked=False, attrs={'rows': '10'}), 
        }
        #         # checkboxes
        #         'outsourced': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'auditRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'bsaRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'cispRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'complianceRiskb': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'redFlagRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
        #         'regulatoryRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 

        #         # 'riskTypes': FilteredSelectMultiple("verbose name", is_stacked=False), 

        # }

