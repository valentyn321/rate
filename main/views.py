from django.shortcuts import render
from .models import Currency
from .forms import CurrencyForm
from django.shortcuts import redirect


def currenties_list(request):
    currenties = Currency.objects.order_by('-selling')
    return render(request, 'main/currenties_list.html', {'currenties':currenties})

def what_rate(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.save()
            return redirect('currenties_list')
    else:
        form = CurrencyForm()
    return render(request, 'main/what_rate.html', {'form': form})
