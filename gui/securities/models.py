from django.db import models


class Company(models.Model):
    name = models.TextField()


class FinancialStatement(models.Model):
    company = models.ForeignKey('Company')
    total_assets = models.FloatField()
    total_current_assets = models.FloatField()
    total_liabilities = models.FloatField()
    total_current_liabilities = models.FloatField()
    debt = models.FloatField()
    net_income = models.FloatField(help_text="Always estimated for the whole year.")
    share_price_soles = models.FloatField()
    total_shares = models.FloatField()
    year = models.ForeignKey('Year')


class Year(models.Model):
    year = models.IntegerField()
