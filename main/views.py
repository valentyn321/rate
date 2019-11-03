from django.shortcuts import render

def currenties_list(request):
    return render(request, 'main/currenties_list.html', {})
