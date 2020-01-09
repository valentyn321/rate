from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.currenties_list, name='currenties_list'),
    path('what_rate', views.what_rate, name='what_rate'),

]