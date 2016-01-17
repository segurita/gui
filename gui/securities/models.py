from django.db import models


class Company(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class FinancialStatement(models.Model):
    company = models.ForeignKey('Company')
    security_code = models.CharField(max_length=200, help_text="Share code: for example continc1")
    year = models.ForeignKey('Year')
    total_assets = models.FloatField()
    total_current_assets = models.FloatField()
    total_liabilities = models.FloatField()
    total_current_liabilities = models.FloatField()
    debt = models.FloatField()
    net_income = models.FloatField(help_text="Always estimated for the whole year.")

    share_price_soles = models.FloatField()
    total_shares = models.FloatField()
    earnings_per_share = models.FloatField()
    pe_ratio = models.FloatField()

    book_value_per_share = models.FloatField()
    net_per_share_by_book_value = models.FloatField()
    price_by_book_value = models.FloatField()
    pe_times_price_by_book_value = models.FloatField()

    net_working_capital = models.FloatField()
    market_price = models.FloatField()

    def __str__(self):
        return "{0} {1} {2}".format(
                self.company,
                self.security_code.upper(),
                self.year,
        )

    def save(self, *args, **kwargs):
        self.earnings_per_share = round(self.net_income / self.total_shares, 1)
        self.pe_ratio = round(float(self.share_price_soles) / self.earnings_per_share, 1)
        self.book_value_per_share = round((self.total_assets - self.total_liabilities) / self.total_shares, 1)
        self.net_per_share_by_book_value = round(self.earnings_per_share * 100 / self.book_value_per_share, 1)
        self.price_by_book_value = round(float(self.share_price_soles) / self.book_value_per_share, 1)
        self.pe_times_price_by_book_value = round(self.pe_ratio * self.price_by_book_value, 1)
        self.net_working_capital = round(self.total_assets - self.total_liabilities, 1)
        self.market_price = round(self.share_price_soles * self.total_shares, 1)
        super(FinancialStatement, self).save(*args, **kwargs)


class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)
