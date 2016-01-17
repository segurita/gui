from django.db import models


class Company(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class FinancialStatement(models.Model):
    company = models.ForeignKey('Company')
    security_code = models.CharField(max_length=200, help_text="Share code: for example continc1")
    total_assets = models.FloatField()
    total_current_assets = models.FloatField()
    total_liabilities = models.FloatField()
    total_current_liabilities = models.FloatField()
    debt = models.FloatField()
    net_income = models.FloatField(help_text="Always estimated for the whole year.")
    share_price_soles = models.FloatField()
    total_shares = models.FloatField()
    year = models.ForeignKey('Year')

    def __str__(self):
        return "{0} {1} {2}".format(self.company, self.security_code.upper(), self.year)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)
