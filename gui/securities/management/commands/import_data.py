import glob
import json
import os

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from securities.models import Company, FinancialStatement, Year


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--folder',
                            action='store',
                            dest='input_folder',
                            help='Enter name of folder containing JSON files to import.'
                            )

    def handle(self, *args, **options):
        if not options['input_folder']:
            raise CommandError("Folder does not exist.")

        input_folder = options['input_folder']
        for filename in glob.glob(os.path.join(input_folder, "*json")):
            self.process_file(filename)

    def process_file(self, filename):
        print(filename)
        if "schema.json" not in filename:
            with open(filename, "r") as handle:
                data = json.loads(handle.read())

            security_code = self.extract_code(filename)
            for item in data:
                self.update_item_in_database(item, security_code)

    def extract_code(self, filename):
        file_path, file_extension = os.path.splitext(filename)
        return os.path.basename(file_path)

    def update_item_in_database(self, item, security_code):
        if security_code == "continc1":
            company_name = "Banco Continental"

        try:
            company = Company.objects.get(name=company_name)
        except ObjectDoesNotExist:
            company = Company(name=company_name)
            company.save()

        item_year = item['year']
        try:
            financial_statement_year = Year.objects.get(year=item_year)
        except ObjectDoesNotExist:
            financial_statement_year = Year(year=item_year)
            financial_statement_year.save()

        try:
            security = FinancialStatement.objects.get(
                company=company,
                security_code=security_code,
                year=financial_statement_year,
            )
        except ObjectDoesNotExist:
            security = FinancialStatement(
                company=company,
                security_code=security_code,
                year=financial_statement_year,
            )

        security.total_assets = item['total_assets']
        security.total_current_assets = item['total_current_assets']
        security.total_liabilities = item['total_liabilities']
        security.total_current_liabilities = item['total_current_liabilities']
        security.debt = item['debt']
        security.net_income = item['net_income']
        security.share_price_soles = item['share_price_soles']
        security.total_shares = item['total_shares']
        security.save()

        print("Updated security: {!r}".format(security))
