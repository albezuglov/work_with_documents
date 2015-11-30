from django.db import models

# Create your models here.
class Contractor (models.Model):
    name = models.CharField(max_length=200)
    shortName = models.CharField(max_length=100)


class BankDetails (models.Model):
    contractor = models.ManyToManyField(Contractor, related_name='bank')
    name = models.CharField(max_length=200)
    mfo = models.PositiveIntegerField()


class AccountingDetails (models.Model):
    contactor = models.ForeignKey(Contractor, related_name='account')
    officialName = models.CharField(max_length=200)
    edprou = models.PositiveIntegerField()
    account = models.PositiveIntegerField()
    address = models.CharField(max_length=200)