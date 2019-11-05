from django.shortcuts import render
from .models import Currency

def currenties_list(request):
    currenties = Currency.objects.order_by('-selling')
    return render(request, 'main/currenties_list.html', {'currenties':currenties})
