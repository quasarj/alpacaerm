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

    # left side

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
        verbose_name="SSAE 16")
    sas70Type = models.CharField(
        verbose_name="SSAE 16 Type",
        max_length=SHORT,
        choices=SAS70_CHOICES)
    sas70Date = models.DateField(
        null=True, blank=True, 
        verbose_name="SSAE 16 Date")
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

    # right side

    exposure = models.FloatField(
        default=0,
        verbose_name="Exposure / Access to Customer Information")
    sensitivity = models.FloatField(
        default=0,
        verbose_name="Sensitivity of Information")
    infoVolume = models.FloatField(
        default=0,
        verbose_name="Volume of Information")
    productInvestment = models.FloatField(
        default=0,
        verbose_name="Investment in Product")
    operationalDependence = models.FloatField(
        default=0,
        verbose_name="Operational Dependence")
    cusomterSupport = models.FloatField(
        default=0,
        verbose_name="Customer Support Response")
    productSecurity = models.FloatField(
        default=0,
        verbose_name="Product Security")
    nondisclosure = models.FloatField(
        default=0,
        verbose_name="Nondisclosure Agreements")
    businessResumption = models.FloatField(
        default=0,
        verbose_name="Business Resumption Plan")
    hiring = models.FloatField(
        default=0,
        verbose_name="Hiring Practices")
    networkSecurity = models.FloatField(
        default=0,
        verbose_name="Network Security / Penetration Testing")
    thirdPartyRelationship = models.FloatField(
        default=0,
        verbose_name="Thid Party Relationship")
    financialStability = models.FloatField(
        default=0,
        verbose_name="Financial Stability")
    sas70Value = models.FloatField(
        default=0,
        verbose_name="SSAE 16")
    independentMonitoring = models.FloatField(
        default=0,
        verbose_name="Independent Monitoring / Reporting")

    # calculated fields
    #TODO: These are not being calculated. Override the save() method
    # of this model to calculate these fields on save!

    vendorRiskRating = models.FloatField(
        default=0,
        verbose_name="Vendor Risk Rating")
    priorRiskRating = models.FloatField(
        default=0,
        verbose_name="Prior Risk Rating")
    inherentRiskRating = models.FloatField(
        default=0,
        verbose_name="Inherent Risk Rating")

    nextReviewDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Next Review Date")
    lastReviewDate = models.DateField(
        null=True, blank=True, 
        verbose_name="Last Review Date")

    def save(self, *args, **kwargs):
        # calculate the calculated fields


        #Inherent Risk Rating
        #TODO: several fields missing here
        inherent_fields = [
            self.exposure,
            self.sensitivity,
            self.infoVolume,
            self.productInvestment,
            self.operationalDependence,
            self.cusomterSupport,
            self.productSecurity,
            self.nondisclosure,
            self.thirdPartyRelationship,
            self.businessResumption,
            self.hiring,
            self.networkSecurity,
            self.independentMonitoring,
        ]
        # average of only the fields with values > 0
        field_count = sum([1 for i in inherent_fields if i > 0])
        if field_count > 0:
            self.inherentRiskRating = sum(inherent_fields) / field_count
        else:
            self.inherentRiskRating = 0


        #calMitigations - used in the calc of vendor risk rating
        mit_fields = [
            self.financialStability,
            self.sas70Value,
        ]
        field_count = sum([1 for i in mit_fields if i > 0])
        if field_count > 0:
            cal_mitigations = sum(mit_fields) / field_count
        else:
            cal_mitigations = 0



        self.priorRiskRating = self.vendorRiskRating
        # vendor risk rating
        self.vendorRiskRating = self.inherentRiskRating * cal_mitigations


        #TODO: these aren't really calculated fields, are they?
        # self.nextReviewDate
        # self.lastReviewDate

        super(Vendor, self).save(*args, **kwargs)

    def trending(self):
        """get the trending status of this vendor"""

        if self.vendorRiskRating > self.priorRiskRating:
            return "High"
        elif self.vendorRiskRating < self.priorRiskRating:
            return "Low"

        # return flat if it isn't anything else, or if there was an error
        return "Flat"

    def __unicode__(self):
        return "{}: {}".format(self.bank, self.name)
