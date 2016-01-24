import glob
import json
import os
import sys

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
        companies = {
            "continc1": "Banco Continental",
            "creditc1": "Banco de Crédito",
            "scotiac1": "Banco Scotiabank",
        }

        try:
            company = Company.objects.get(name=companies[security_code])
        except KeyError:
            print("\nSecurity code {!r} does not match any company. Add it to "
                  "this script (line 42)".format(security_code))
            sys.exit(1)
        except ObjectDoesNotExist:
            company = Company(name=companies[security_code])
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

        security.total_assets = round(item['total_assets'], 1)
        security.total_current_assets = round(item['total_current_assets'], 1)
        security.total_liabilities = round(item['total_liabilities'], 1)
        security.total_current_liabilities = round(item['total_current_liabilities'], 1)
        security.debt = round(item['debt'], 1)
        security.net_income = round(item['net_income'], 1)
        security.share_price_soles = round(item['share_price_soles'], 1)
        security.total_shares = round(item['total_shares'], 1)
        security.save()

        print("Updated security: {!r}\n".format(security))
