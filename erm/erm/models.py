from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


BIGTEXT_LEN=5000

class Bank(models.Model):
    name = models.CharField(max_length=200)
    report_risk_ass_ratings_message = models.CharField(max_length=5000, default="No text")
    report_risk_scoring_by_source_message = models.CharField(max_length=5000, default="No text")
    report_vendor_ass_message = models.CharField(max_length=5000, default="No text")
    report_dist_by_type_message = models.CharField(max_length=5000, default="No text")
    report_class_by_bu_message = models.CharField(max_length=5000, default="No text")
    report_action_items_summary_message = models.CharField(max_length=5000, default="No text")
    report_summary_conclusions_message = models.CharField(max_length=5000, default="No text")
    report_footer_message = models.CharField(max_length=5000, default="No text")

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

class RiskManager(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class BankRisk(models.Model):

    bank = models.ForeignKey(Bank)

    name = models.CharField(max_length=200)

    reviewDate = models.DateField(null=True, 
                                  blank=True, 
                                  verbose_name="Last Review Date")

    riskTypes = models.ManyToManyField(
            RiskType, 
            null=True, 
            verbose_name='Risk Types')


    riskSources = models.ManyToManyField(RiskSource, null=True,
            verbose_name='Risk Sources')

    riskManagers = models.ManyToManyField(RiskManager, null=True,
            verbose_name='Risk Managers')

    # fields from the Detail table in Access
    riskText = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name='Systems or Assets at Risk')
    location = models.CharField(max_length=200, null=True, blank=True,
            verbose_name= 'Location of Systems or Assets')
    threat = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name= 'Detail of Source of Threat or Vulnerability')
    response = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name= 'Detail of Incident Response')
    mitigations = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name= 'Controls and Other Risk Mitigation Factors')
    comments = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name='Comments')
    customers = models.FloatField(default=0,
            verbose_name= 'Impact to Customer')
    impact = models.FloatField(default=0,
            verbose_name= 'Impact to Organization')
    controls = models.FloatField(default=0,
            verbose_name= 'Controls Rating')
    controlsWeight = models.FloatField(default=0,
            verbose_name= 'Controls Rating Weight')
    policyRate = models.FloatField(default=0,
            verbose_name= 'Policy Rating')
    policyWeight = models.FloatField(default=0,
            verbose_name= 'Policy Rating Weight')
    inherentRisk = models.FloatField(default=0,
            verbose_name= 'Inherent Risk')
    vendorRisk = models.FloatField(default=0,
            verbose_name= 'Vendor Risk')
    vendorRiskWeight = models.FloatField(default=0,
            verbose_name= 'Vendor Risk Weight')
    marketRisk = models.FloatField(default=0,
            verbose_name= 'Market Risk')
    marketRiskWeight = models.FloatField(default=0,
            verbose_name= 'Market Risk Weight')
    operationalRisk = models.FloatField(default=0,
            verbose_name= 'Operational Risk')
    operationalRiskWeight = models.FloatField(default=0,
            verbose_name= 'Operational Risk Weight')
    complianceRisk = models.FloatField(default=0,
            verbose_name= 'Compliance Risk')
    complianceRiskWeight = models.FloatField(default=0,
            verbose_name= 'Compliance Risk Weight')
    strategicRisk = models.FloatField(default=0,
            verbose_name= 'Strategic Risk')
    strategicRiskWeight = models.FloatField(default=0,
            verbose_name= 'Strategic Risk Weight')
    reputationRisk = models.FloatField(default=0,
            verbose_name= 'Reputational Risk')
    reputationRiskWeight = models.FloatField(default=0,
            verbose_name= 'Reputational Risk Weight')
    creditRisk = models.FloatField(default=0,
            verbose_name= 'Credit Risk')
    creditRiskWeight = models.FloatField(default=0,
            verbose_name= 'Credit Risk Weight')
    fiduciaryRisk = models.FloatField(default=0,
            verbose_name= 'Fiduciary Risk')
    fiduciaryRiskWeight = models.FloatField(default=0,
            verbose_name= 'Fiduciary Risk Weight')
    regulatoryLegalRisk = models.FloatField(default=0,
            verbose_name= 'Regulatory Legal Risk')
    regulatoryLegalRiskWeight = models.FloatField(default=0,
            verbose_name= 'Regulatory Legal Risk Weight')
    humanResourceRisk = models.FloatField(default=0,
            verbose_name= 'Human Resource Risk')
    humanResourceRiskWeight = models.FloatField(default=0,
            verbose_name= 'Human Resource Risk Weight')
    compositeRisk = models.FloatField(default=0)
    riskRating = models.FloatField(default=0)
    lastCompositeRisk = models.FloatField(default=0)
    lastRiskRating = models.FloatField(default=0)
    bsaRisk = models.BooleanField(
            verbose_name= 'BSA / AML / OFAC Risk Management')
    regulatoryRisk = models.BooleanField(
            verbose_name= 'Regulatory Risk Management')
    cispRisk = models.BooleanField(
            verbose_name= 'CISP Risk Management')
    auditRisk = models.BooleanField(
            verbose_name= 'Audit Risk Management')
    complianceRiskb = models.BooleanField(
            verbose_name= 'Compliance Risk Management')
    redFlagRisk = models.BooleanField(
            verbose_name= 'Red Flag Risk Management')
    outsourced = models.BooleanField(
            verbose_name= 'Outsourced Service')
    # RiskManagerDet
    # RiskManager2Det
    # RiskManager3Det
    # RiskManager4Det
    # PolicyDet
    # Policy2Det
    # Policy3Det
    # Policy4Det
    frequencyDet = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True,
            verbose_name= 'Frequency')
    # priorRating = models.FloatField(default=0)
    # intpriorrating = models.FloatField(default=0)
    # trend = models.CharField(max_length=2000, null=True, blank=True)
    # LastReviewer
    # PriorRatingCalc
    # RiskTypeDet
    # Required
    # calInherentRiskRating = models.FloatField(default=0)
    
    def calc_composite_risk(self):
        """calculate the composite risk"""
        # NOTE: This needs to decide which risks to actually
        # use based on the RiskType field!

        # risks to use from original calc (legacy app)
        vendor = self.vendorRisk * self.vendorRiskWeight
        market = self.marketRisk * self.marketRiskWeight
        operational = self.operationalRisk * self.operationalRiskWeight
        compliance = self.complianceRisk * self.complianceRiskWeight
        strategic = self.strategicRisk * self.strategicRiskWeight
        reputation = self.reputationRisk * self.reputationRiskWeight
        credit = self.creditRisk * self.creditRiskWeight
        fiduciary = self.fiduciaryRisk * self.fiduciaryRiskWeight
        regulatory = self.regulatoryLegalRisk * self.regulatoryLegalRiskWeight
        humanResource = self.humanResourceRisk * self.humanResourceRiskWeight

        total = (   vendor +
                    market +
                    operational +
                    compliance +
                    strategic +
                    reputation +
                    credit +
                    fiduciary +
                    regulatory +
                    humanResource   )

        weights = (
            self.vendorRiskWeight +
            self.marketRiskWeight +
            self.operationalRiskWeight +
            self.complianceRiskWeight +
            self.strategicRiskWeight +
            self.reputationRiskWeight +
            self.creditRiskWeight +
            self.fiduciaryRiskWeight +
            self.regulatoryLegalRiskWeight +
            self.humanResourceRiskWeight
        )

        return total / weights

    def calc_risk_rating(self):
        """calculate the rating of this risk"""
        # TODO: write this

        calc = (
            self.customers +
            self.impact +
            self.inherentRisk + 
            self.compositeRisk
        ) / 4.0

        calc *= ((
            (self.controls * self.controlsWeight) +
            (self.policyRate * self.policyWeight)
        ) / (self.controlsWeight + self.policyWeight))

        return calc

    def save(self, *args, **kwargs):
        # calculate the calculated fields
        self.lastRiskRating = self.riskRating
        self.riskRating = self.calc_risk_rating()

        self.lastCompositeRisk = self.compositeRisk
        self.compositeRisk = self.calc_composite_risk()

        super(BankRisk, self).save(*args, **kwargs)


    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.name)



    def trending(self):
        """get the trending status of this risk
        based on the last history item"""

        if self.riskRating > self.lastRiskRating:
            return "High"
        elif self.riskRating < self.lastRiskRating:
            return "Low"

        # return flat if it isn't anything else, or if there was an error
        return "Flat"


# a RiskProfile is a set of risks that can be assigned to a bank
# all at once
class RiskProfile(models.Model):
    name = models.CharField(max_length=200)
    risks = models.ManyToManyField(BankRisk)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    # link to the actual user
    user = models.OneToOneField(User)
    level = models.SmallIntegerField(null=False, 
                                     help_text="0 for read-only, 1 for update, 2 for admin")

    # extend with new data
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.user.username)

    def is_active(self):
        if self.user.is_active:
            return "Yes"
        else:
            return "No"

    def get_level(self):
        return {0: "Read Only",
                1: "Update",
                2: "Admin" }[self.level]



