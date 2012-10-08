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

    def __init__(self, *args, **kwargs):
        super(BankRiskForm, self).__init__(*args, **kwargs)
        self.fix_names()

    def fix_names(self):
        """hack to fix field labels"""
        # For some reason with Django 1.4 I can't
        # change the label of a field and also set
        # a custom "widget", so this method (and the __init__)
        # sets field labels after the form is built

        #TODO: turns out I was wrong here, and we just need to set the
        # verbose_name field on the model
        
        labels = {
            'reviewDate': 'Last Review Date',
            'riskTypes': 'Risk Types',
            'riskSources': 'Risk Sources',
            'riskText': 'Systems or Assets at Risk',
            'location': 'Location of Systems or Assets',
            'threat': 'Detail of Source of Threat or Vulnerability',
            'response': 'Detail of Incident Response',
            'mitigations': 'Controls and Other Risk Mitigation Factors',

            'customers': 'Impact to Customer',
            'impact': 'Impact to Organization',
            'controls': 'Controls Rating',
            'controlsWeight': 'Controls Rating Weight',
            'policyRate': 'Policy Rating',
            'policyWeight': 'Policy Rating Weight',
            'inherentRisk': 'Inherent Risk',
            'vendorRisk': 'Vendor Risk',
            'vendorRiskWeight': 'Vendor Risk Weight',
            'marketRisk': 'Market Risk',
            'marketRiskWeight': 'Market Risk Weight',
            'operationalRisk': 'Operational Risk',
            'operationalRiskWeight': 'Operational Risk Weight',
            'complianceRisk': 'Compliance Risk',
            'complianceRiskWeight': 'Compliance Risk Weight',
            'strategicRisk': 'Strategic Risk',
            'strategicRiskWeight': 'Strategic Risk Weight',
            'reputationRisk': 'Reputational Risk',
            'reputationRiskWeight': 'Reputational Risk Weight',
            'creditRisk': 'Credit Risk',
            'creditRiskWeight': 'Credit Risk Weight',
            'fiduciaryRisk': 'Fiduciary Risk',
            'fiduciaryRiskWeight': 'Fiduciary Risk Weight',
            'regulatoryLegalRisk': 'Regulatory Legal Risk',
            'regulatoryLegalRiskWeight': 'Regulatory Legal Risk Weight',
            'humanResourceRisk': 'Human Resource Risk',
            'humanResourceRiskWeight': 'Human Resource Risk Weight',
            # 'compositeRisk': 'Composite Risk Weight',
            # 'riskRating': 'Risk Rating',

            'outsourced': 'Outsourced Service',
            'auditRisk': 'Audit Risk Management',
            'bsaRisk': 'BSA / AML / OFAC Risk Management',
            'cispRisk': 'CISP Risk Management',
            'complianceRiskb': 'Compliance Risk Management',
            'redFlagRisk': 'Red Flag Risk Management',
            'regulatoryRisk': 'Regulatory Risk Management',


            'frequencyDet': 'Frequency',
        }

        # assign to the real fields
        for k in labels.keys():
            self.fields[k].label = labels[k]


    class Meta:
        model = BankRisk
        exclude = ('bank', 'risk')
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

