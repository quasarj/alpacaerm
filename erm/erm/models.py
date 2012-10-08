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


class AbstractRisk(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=200)

    reviewDate = models.DateField(null=True, blank=True)

    riskTypes = models.ManyToManyField(RiskType, null=True)
    riskSources = models.ManyToManyField(RiskSource, null=True)

    riskManagers = models.ManyToManyField(RiskManager, null=True)

    # fields from the Detail table in Access
    riskText = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    threat = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
    response = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
    mitigations = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
    comments = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
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
    # compositeRisk = models.FloatField(default=0)
    # riskRating = models.FloatField(default=0)
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
    frequencyDet = models.CharField(max_length=BIGTEXT_LEN, null=True, blank=True)
    # priorRating = models.FloatField(default=0)
    # intpriorrating = models.FloatField(default=0)
    # trend = models.CharField(max_length=2000, null=True, blank=True)
    # LastReviewer
    # PriorRatingCalc
    # RiskTypeDet
    # Required
    # calInherentRiskRating = models.FloatField(default=0)
    
    def compositeRisk(self):
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

    def riskRating(self):
        """calculate the rating of this risk"""
        # TODO: write this


        calc = (
            self.customers +
            self.impact +
            self.inherentRisk + 
            self.compositeRisk()
        ) / 4.0

        calc *= ((
            (self.controls * self.controlsWeight) +
            (self.policyRate * self.policyWeight)
        ) / (self.controlsWeight + self.policyWeight))

        return calc


class Risk(AbstractRisk):

    def __unicode__(self):
        return self.name

class BankRisk(AbstractRisk):
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.name)


    def trending(self):
        """get the trending status of this risk
        based on the last history item"""

        # dummy implementation at this point
        hists = self.bankriskhistory_set.all()
        if len(hists) > 0:
            last_rating = hists[hists.count() - 1].riskRating()
            rating = self.riskRating()

            if rating > last_rating:
                return "High"
            elif rating < last_rating:
                return "Low"

        # return flat if it isn't anything else, or if there was an error
        return "Flat"

class BankRiskHistory(AbstractRisk):
    bankRisk = models.ForeignKey(BankRisk)
    saved_time = models.DateTimeField()

    def load(self, bankrisk=None):
        """load data from a bankrisk"""

        if bankrisk:
            # attempt to copy the BankRisk data

            # ugly hack to copy from one model to another
            for attr in bankrisk.__dict__:
                if attr != '_state' and attr != 'id':
                    setattr(self, attr, getattr(bankrisk, attr))

            self.bankRisk = bankrisk
            self.saved_time = timezone.now()

            # the above trick doesn't work for 
            # many-to-many relationships, so do them
            # manually here.
            # Also, the object must be saved before
            # m2m relaitonships can be added
            self.save()

            for rm in bankrisk.riskManagers.all():
                self.riskManagers.add(rm)

            for rt in bankrisk.riskTypes.all():
                self.riskTypes.add(rt)

            for rs in bankrisk.riskSources.all():
                self.riskSources.add(rs)

    def __unicode__(self):
        return "{}: {}".format(self.bankRisk.id, self.saved_time)

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
                                     help_text="0 for read-only, 1 for update, 2 for admin")

    # extend with new data
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.user.username)



