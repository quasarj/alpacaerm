from django.forms import Textarea
from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from erm.models import *


## ReportEditTextForm
class ReportEditTextForm(ModelForm):

    class Meta:
        model = Bank
        exclude = ('name', )

        widgets = {
                # large text inputs
                'report_risk_ass_ratings_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_risk_scoring_by_source_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_vendor_ass_message' : Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_dist_by_type_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_class_by_bu_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_action_items_summary_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_summary_conclusions_message': Textarea(attrs={'cols': 80, 'rows': 10}),
                'report_footer_message': Textarea(attrs={'cols': 80, 'rows': 10}),
        }


## BankRiskForm

CHECKBOX_ATTRS = {'class': 'risk_checkbox'}
RISK_ATTRS = {'class': 'risk_risk', 'size': 4}
WEIGHT_ATTRS = {'class': 'risk_weight', 'size': 4}

class BankRiskForm(ModelForm):
    # threat = forms.CharField(label='Test Threat Text')

    class Meta:
        model = BankRisk
        exclude = (
            'bank', 
            'risk', 
            'compositeRisk', 
            'lastCompositeRisk', 
            'riskRating', 
            'lastRiskRating',
            'inherentRisk',
        )
        widgets = {
                # large text inputs
                'name': forms.TextInput(attrs={'size': 60}),
                'riskText': Textarea(attrs={'cols': 80, 'rows': 10}),
                'location': forms.TextInput(attrs={'size': 104}),
                'threat': Textarea(attrs={'cols': 80, 'rows': 10}),
                'response': Textarea(attrs={'cols': 80, 'rows': 10}),
                'mitigations': Textarea(attrs={'cols': 80, 'rows': 10}),
                'comments': Textarea(attrs={'cols': 80, 'rows': 10}),
                # 'frequencyDet': Textarea(attrs={'cols': 80, 'rows': 10}),
                # 'trend': Textarea(attrs={'cols': 80, 'rows': 10}),


                # weights
                'customers': forms.TextInput(attrs=RISK_ATTRS),
                'impact': forms.TextInput(attrs=RISK_ATTRS),
                'controls': forms.TextInput(attrs=RISK_ATTRS),
                'controlsWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'policyRate': forms.TextInput(attrs=RISK_ATTRS),
                'policyWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'inherentRisk': forms.TextInput(attrs=RISK_ATTRS),
                'vendorRisk': forms.TextInput(attrs=RISK_ATTRS),
                'vendorRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'marketRisk': forms.TextInput(attrs=RISK_ATTRS),
                'marketRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'operationalRisk': forms.TextInput(attrs=RISK_ATTRS),
                'operationalRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'complianceRisk': forms.TextInput(attrs=RISK_ATTRS),
                'complianceRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'strategicRisk': forms.TextInput(attrs=RISK_ATTRS),
                'strategicRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'reputationRisk': forms.TextInput(attrs=RISK_ATTRS),
                'reputationRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'creditRisk': forms.TextInput(attrs=RISK_ATTRS),
                'creditRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'fiduciaryRisk': forms.TextInput(attrs=RISK_ATTRS),
                'fiduciaryRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'regulatoryLegalRisk': forms.TextInput(attrs=RISK_ATTRS),
                'regulatoryLegalRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                'humanResourceRisk': forms.TextInput(attrs=RISK_ATTRS),
                'humanResourceRiskWeight': forms.TextInput(attrs=WEIGHT_ATTRS),
                # 'compositeRisk': forms.TextInput(attrs=RISK_ATTRS),
                # 'riskRating': forms.TextInput(attrs=RISK_ATTRS),

                # checkboxes
                'outsourced': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'auditRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'bsaRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'cispRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'complianceRiskb': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'redFlagRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'regulatoryRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 

                # 'riskTypes': FilteredSelectMultiple("verbose name", is_stacked=False), 

        }

