from django.shortcuts import render

from securities.models import Company


def home(request):
    context = Company.objects.all()
    print(context)
    return render(request, 'securities/home.html', context)
