from django.db import models

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone

from erm.models import Bank

SHORT=200
LONG=2000

CLASS_CHOICES = (
    (5, 'Mission Critical'),
    (4, 'Mission Critical / Outsourced Services'),
    (3, 'Outsourced Services'),
    (2, 'Access to Customer Information - Not Reviewed'),
    (1, 'Not Classified'),
)

SAS70_CHOICES = (
    ('soc1', 'SOC 1'),
    ('soc2', 'SOC 2'),
    ('soc3', 'SOC 3'),
)

PERIOD_CHOICES = (
    (3, 'Years'),
    (2, 'Months'),
    (1, 'Days'),
)

class Vendor(models.Model):
    bank = models.ForeignKey(Bank)

    name = models.CharField(verbose_name="Vendor Name", max_length=SHORT)
    product = models.CharField(verbose_name="Products or Services Provided", 
                               max_length=LONG)
    classification = models.SmallIntegerField(choices=CLASS_CHOICES,
                                            verbose_name="Classification")
    incidentClause = models.CharField(
        verbose_name="Reporting or Security Incident Clause", 
        max_length=SHORT)
    customerInfo = models.CharField(
        verbose_name="Access to Customer Information",
        max_length=SHORT)
    glba501b = models.CharField(
        verbose_name="GLBA 501(b)",
        max_length=SHORT)
    drTesting = models.CharField(
        verbose_name="Disaster Recovery Testing",
        max_length=SHORT)
    fStatement = models.BooleanField(
        verbose_name="Financial Statement")
    fStatementDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Financial Statement Date")
    sas70 = models.BooleanField(
        verbose_name="SAS 70")
    sas70Type = models.CharField(
        verbose_name="SAS 70 Type",
        max_length=SHORT,
        choices=SAS70_CHOICES)
    sas70Date = models.DateField(
        null=True, blank=True, 
        verbose_name="SAS 70 Date")
    escrow = models.BooleanField(
        verbose_name="Escrow Agreement")
    lastEscrowReviewDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Last Independent Review")
    escrowLocation = models.CharField(
        verbose_name="Escrow Location",
        max_length=SHORT)
    thirdParty = models.BooleanField(
        verbose_name="Third party Relationship")
    thirdPartyName = models.CharField(
        verbose_name="Third Party Relationship Name",
        max_length=SHORT)
    nextRenewalDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Next Contract Renewal Date")
    termNotice = models.SmallIntegerField(
        verbose_name="Termination Notice")
    termNoticePeriod = models.SmallIntegerField(
        choices=PERIOD_CHOICES,
        verbose_name="Termination Notice Period")

    origContractDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Original Contract Date")
    origContractTerm = models.SmallIntegerField(
        verbose_name="Contract Term")
    origContractTermPeriod = models.SmallIntegerField(
        choices=PERIOD_CHOICES,
        verbose_name="Contract Term Period")


    autoRenew = models.BooleanField(
        verbose_name="Auto Renewable")
    autoRenewTerm = models.SmallIntegerField(
        verbose_name="Renewal Term")
    autoRenewTermPeriod = models.SmallIntegerField(
        choices=PERIOD_CHOICES,
        verbose_name="Renewal Term Period")

    comments = models.CharField(
        verbose_name="Comments", 
        max_length=LONG)

