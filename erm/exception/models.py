from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone

from erm.models import RiskSource

class Exception(models.Model):

    # this will actually need to be a foreign key with a new model!
    auditAgency = models.CharField(max_length=200)
    actionItem = models.CharField(max_length=2000)
    recommendation = models.CharField(max_length=2000)
    managementResponse = models.CharField(max_length=2000)
    remediation = models.CharField(max_length=2000)
   
    # these two should have a list of options, but stored as integers
    inherentRisk = models.SmallIntegerField()
    exposureRisk = models.SmallIntegerField()

    riskSources = models.ManyToManyField(RiskSource, null=True)
    
    # should be picked from a list of options?
    status = models.CharField(max_length=200)

    auditReviewDate = models.DateField(null=True, blank=True)
    targetDate = models.DateField(null=True, blank=True)
    completionDate = models.DateField(null=True, blank=True)

    # not sure what to do with this, free form is wrong 
    responsibleParty = models.CharField(max_length=200)

    comments = models.CharField(max_length=4000)


    def compositeRiskScore(self):
        return (self.inherentRisk + self.exposureRisk) / 2

    def __unicode__(self):
        return self.actionItem

