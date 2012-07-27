from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone

from erm.models import RiskSource, Bank

class Agency(models.Model):
    bank = models.ForeignKey(Bank)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('closed_itsc', 'Closed - Pending ITSC Approval'),
    ('closed_assumed', 'Closed - Assumed Risk'),
)
INHERENT_RISK_CHOICES = (
    (5, 'Repeat Finding'),
    (4, 'Requires Immediate Attention (MRIA)'),
    (3, 'Requires Attention (MRA)'),
    (2, 'Observation'),
    (1, 'Comment'),
)
EXPOSURE_RISK_CHOICES = (
    (5, 'Very High'),
    (4, 'High'),
    (3, 'Moderate'),
    (2, 'Low'),
    (1, 'Minimal'),
)

class Exception(models.Model):
     
    bank = models.ForeignKey(Bank)

    actionItem = models.CharField(verbose_name="Action Items, Area of Concern, or Comment", max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    auditAgency = models.ForeignKey(Agency, verbose_name="Audit Agency")
    recommendation = models.CharField(max_length=2000)
    managementResponse = models.CharField(max_length=2000, verbose_name="Management Response")
    remediation = models.CharField(max_length=2000)
   
    # these two should have a list of options, but stored as integers
    inherentRisk = models.SmallIntegerField(choices=INHERENT_RISK_CHOICES,
                                            verbose_name="Inherent Risk")
    exposureRisk = models.SmallIntegerField(choices=EXPOSURE_RISK_CHOICES,
                                            verbose_name="Exposure Risk")

    riskSources = models.ManyToManyField(RiskSource, null=True,
                                         verbose_name="Associated Risk Source")
    

    auditReviewDate = models.DateField(null=True, blank=True,
                                       verbose_name="Audit Review Date")
    targetDate = models.DateField(null=True, blank=True, 
                                  verbose_name="Target Date")
    completionDate = models.DateField(null=True, blank=True,
                                      verbose_name="Completion Date")

    # not sure what to do with this, free form is wrong 
    responsibleParty = models.CharField(max_length=200,
                                        verbose_name="Responsible Party")

    comments = models.CharField(max_length=4000, null=True, blank=True)


    def compositeRiskScore(self):
        return (self.inherentRisk + self.exposureRisk) / 2

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.actionItem)


