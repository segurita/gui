from django.shortcuts import render

from securities.models import FinancialStatement, Year


def home(request):
    year = Year.objects.all().order_by('-year')[0]
    financial_statements = FinancialStatement.objects.all().filter(year=year)
    context = {'result': financial_statements}
    return render(request, 'securities/home.html', context)


def security(request, security_code):
    security = FinancialStatement.objects.all().filter(security_code=security_code)
    context = {'result': security}
    return render(request, 'securities/security_full.html', context)
