from django.shortcuts import render
from .models import Currency
from .forms import CurrencyForm
import urllib.request, json

from django.shortcuts import redirect

jsonurl = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
response = urllib.request.urlopen(jsonurl)
data = json.loads(response.content.decode('utf-8'))


def currenties_list(request):
    currenties = Currency.objects.order_by('-selling')
    return render(request, 'main/currenties_list.html', {'currenties':currenties})

def what_rate(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data
            if(rate["name"].upper() == "USD/UAH"):
                purchase = data[0]['buy']
                selling = data[0]['sale']
                return render(request, 'main/what_rate.html', locals())

            elif(rate["name"].upper() == "EUR/UAH"):
                purchase = data[1]['buy']
                selling = data[1]['sale']
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "RUR/UAH"):
                purchase = data[2]['buy']
                selling = data[2]['sale']
                return render(request, 'main/what_rate.html', locals())
            else:
                return render(request, 'main/what_rate.html', locals())
    else:
        form = CurrencyForm()
    return render(request, 'main/what_rate.html', {'form': form})
