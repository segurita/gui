from django.shortcuts import render

from securities.models import FinancialStatement


def home(request):
    financial_statements = FinancialStatement.objects.all().filter(year__year=2015)
    context = {'result': financial_statements}
    return render(request, 'securities/home.html', context)
