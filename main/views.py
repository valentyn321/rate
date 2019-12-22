from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Currency
from .forms import CurrencyForm
from django.contrib.auth.decorators import login_required
import urllib, json
import urllib.request
from django.template.loader import render_to_string
from django.views.generic import FormView





jsonurl = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"

with urllib.request.urlopen(jsonurl) as url:
    data = json.loads(url.read().decode())


def currenties_list(request):
    currenties = Currency.objects.order_by('-selling')
    return render(request, 'main/currenties_list.html', {'currenties':currenties}) 

'''session_key = request.session.session_key
if not session_key:
    request.session.cycle_key()    '''

@login_required
def what_rate(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data
            if(rate["name"].upper() == "USD/UAH"):
                purchase = data[0]["buy"]
                selling = data[0]["sale"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "EUR/UAH"):
                purchase = data[1]["buy"]
                selling = data[1]["sale"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "RUB/UAH"):
                purchase = data[2]["buy"]
                selling = data[2]["sale"]
                return render(request, 'main/what_rate.html', locals())
            elif(rate["name"].upper() == "BTC/UAH"):
                purchase = data[3]["buy"]
                selling = data[3]["sale"]
                return render(request, 'main/what_rate.html', locals())
        else:
            print(rate)
            return render(request, 'main/what_rate.html', locals())
    else:
        form = CurrencyForm()
    return render(request, 'main/what_rate.html', {'form': form})


def ajax(request):
    if request.is_ajax():
        response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}
        return JsonResponse(response)
    else:
        return Http404
        
