from django.shortcuts import render
from .models import Currency
from .forms import CurrencyForm
import urllib, json
import urllib.request as ur
import urllib.parse as par
from django.shortcuts import redirect

jsonurl = "http://resources.finance.ua/ua/public/currency-cash.json"
html = ur.urlopen(jsonurl).read()
data = json.loads(html.decode('utf-8'))

def currenties_list(request):
    currenties = Currency.objects.order_by('-selling')
    return render(request, 'main/currenties_list.html', {'currenties':currenties})

def what_rate(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data
            if(rate["name"].upper() == "USD/UAH"):
                purchase = data["organizations"][0]["currencies"]["USD"]["bid"]
                selling = data["organizations"][0]["currencies"]["USD"]["ask"]
                return render(request, 'main/what_rate.html', locals())

            elif(rate["name"].upper() == "EUR/UAH"):
                purchase = data["organizations"][0]["currencies"]["EUR"]["bid"]
                selling = data["organizations"][0]["currencies"]["EUR"]["ask"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "RUB/UAH"):
                purchase = data["organizations"][0]["currencies"]["RUB"]["bid"]
                selling = data["organizations"][0]["currencies"]["RUB"]["ask"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "GBP/UAH"):
                purchase = data["organizations"][1]["currencies"]["GBP"]["bid"]
                selling = data["organizations"][1]["currencies"]["GBP"]["ask"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "CAD/UAH"):
                purchase = data["organizations"][1]["currencies"]["CAD"]["bid"]
                selling = data["organizations"][1]["currencies"]["CAD"]["ask"]
                return render(request, 'main/what_rate.html', locals())
            else:
                return render(request, 'main/what_rate.html', locals())
    else:
        form = CurrencyForm()
    return render(request, 'main/what_rate.html', {'form': form})
