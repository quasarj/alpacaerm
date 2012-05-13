from django.db import models
from django.contrib.auth.models import User


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

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.risk.title)

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

    # extend with new data
    bank = models.ForeignKey(Bank)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.user.username)


