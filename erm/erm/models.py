from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Risk(models.Model):
    bank = models.ForeignKey(Bank)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return "{}: {}".format(self.bank.name, self.title)

# a RiskProfile is a set of risks that can be assigned to a bank
# all at once
class RiskProfile(models.Model):
    name = models.CharField(max_length=200)
    risks = models.ManyToManyField(Risk)

