from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Risk(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class BankRisk(models.Model):
    bank = models.ForeignKey(Bank)
    risk = models.ForeignKey(Risk)

    # fields from the Detail table in Access
    threat = models.CharField(max_length=200, null=True)
    riskText = models.CharField(max_length=200, null=True)
    mitigations = models.CharField(max_length=200, null=True)
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
    reviewDate = models.DateField(null=True)
    bsaRisk = models.BooleanField()
    regulatoryRisk = models.BooleanField()
    cispRisk = models.BooleanField()
    auditRisk = models.BooleanField()
    complianceRisk = models.BooleanField()
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
    frequencyDet = models.CharField(max_length=200, null=True)
    priorRating = models.FloatField(default=0)
    intpriorrating = models.FloatField(default=0)
    comments = models.CharField(max_length=900, null=True)
    trend = models.CharField(max_length=200, null=True)
    # LastReviewer
    # PriorRatingCalc
    # RiskTypeDet
    # Required
    calInherentRiskRating = models.FloatField(default=0)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.risk.title)

    class Meta:
        unique_together = (("bank", "risk"),)

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
class BankRiskForm(ModelForm):
    class Meta:
        model = BankRisk
        exclude = ('bank', 'risk')

