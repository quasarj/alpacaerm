from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class RiskType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class RiskSource(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class AbstractRisk(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=200)

    reviewDate = models.DateField(null=True, blank=True)

    riskType = models.ForeignKey(RiskType, null=True)
    riskSource = models.ForeignKey(RiskSource, null=True)

    # fields from the Detail table in Access
    riskText = models.CharField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    threat = models.CharField(max_length=2000, null=True, blank=True)
    response = models.CharField(max_length=2000, null=True, blank=True)
    mitigations = models.CharField(max_length=2000, null=True, blank=True)
    comments = models.CharField(max_length=2000, null=True, blank=True)
    customers = models.FloatField(default=0)
    impact = models.FloatField(default=0)
    controls = models.FloatField(default=0)
    controlsWeight = models.FloatField(default=0)
    policyRate = models.FloatField(default=0)
    policyWeight = models.FloatField(default=0)
    inherentRisk = models.FloatField(default=0)
    vendorRisk = models.FloatField(default=0)
    vendorRiskWeight = models.FloatField(default=0)
    marketRisk = models.FloatField(default=0)
    marketRiskWeight = models.FloatField(default=0)
    operationalRisk = models.FloatField(default=0)
    operationalRiskWeight = models.FloatField(default=0)
    complianceRisk = models.FloatField(default=0)
    complianceRiskWeight = models.FloatField(default=0)
    strategicRisk = models.FloatField(default=0)
    strategicRiskWeight = models.FloatField(default=0)
    reputationRisk = models.FloatField(default=0)
    reputationRiskWeight = models.FloatField(default=0)
    creditRisk = models.FloatField(default=0)
    creditRiskWeight = models.FloatField(default=0)
    fiduciaryRisk = models.FloatField(default=0)
    fiduciaryRiskWeight = models.FloatField(default=0)
    regulatoryLegalRisk = models.FloatField(default=0)
    regulatoryLegalRiskWeight = models.FloatField(default=0)
    humanResourceRisk = models.FloatField(default=0)
    humanResourceRiskWeight = models.FloatField(default=0)
    compositeRisk = models.FloatField(default=0)
    riskRating = models.FloatField(default=0)
    bsaRisk = models.BooleanField()
    regulatoryRisk = models.BooleanField()
    cispRisk = models.BooleanField()
    auditRisk = models.BooleanField()
    complianceRiskb = models.BooleanField()
    redFlagRisk = models.BooleanField()
    outsourced = models.BooleanField()
    # RiskManagerDet
    # RiskManager2Det
    # RiskManager3Det
    # RiskManager4Det
    # PolicyDet
    # Policy2Det
    # Policy3Det
    # Policy4Det
    frequencyDet = models.CharField(max_length=2000, null=True, blank=True)
    priorRating = models.FloatField(default=0)
    intpriorrating = models.FloatField(default=0)
    trend = models.CharField(max_length=2000, null=True, blank=True)
    # LastReviewer
    # PriorRatingCalc
    # RiskTypeDet
    # Required
    calInherentRiskRating = models.FloatField(default=0)


class Risk(AbstractRisk):

    def __unicode__(self):
        return self.name

class BankRisk(AbstractRisk):
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.name)

#    class Meta:
#        unique_together = (("bank", "risk"),)

# a RiskProfile is a set of risks that can be assigned to a bank
# all at once
class RiskProfile(models.Model):
    name = models.CharField(max_length=200)
    risks = models.ManyToManyField(Risk)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    # link to the actual user
    user = models.OneToOneField(User)
    level = models.SmallIntegerField(null=False, 
                                     help_text="0 for read-only, 1 for full access")

    # extend with new data
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.user.username)



# Forms
from django.forms import Textarea
from django import forms


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
        
        labels = {
            'reviewDate': 'Last Review Date',
            'riskType': 'Risk Type',
            'riskSource': 'Risk Source',
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
            'compositeRisk': 'Composite Risk Weight',
            'riskRating': 'Risk Rating',

            'outsourced': 'Outsourced Service',
            'auditRisk': 'Audit Risk Management',
            'bsaRisk': 'BSA / AML / OFAC Risk Management',
            'cispRisk': 'CISP Risk Management',
            'complianceRiskb': 'Compliance Risk Management',
            'redFlagRisk': 'Red Flag Risk Management',
            'regulatoryRisk': 'Regulatory Risk Management',

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
                'frequencyDet': Textarea(attrs={'cols': 80, 'rows': 10}),
                'trend': Textarea(attrs={'cols': 80, 'rows': 10}),


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
                'compositeRisk': forms.TextInput(attrs=RISK_ATTRS),
                'riskRating': forms.TextInput(attrs=RISK_ATTRS),

                # checkboxes
                'outsourced': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'auditRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'bsaRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'cispRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'complianceRiskb': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'redFlagRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 
                'regulatoryRisk': forms.CheckboxInput(attrs=CHECKBOX_ATTRS), 

        }

