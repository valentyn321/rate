from django.urls import path
from . import views

urlpatterns = [
    path('', views.currenties_list, name='currenties_list'),
    path('what_rate', views.what_rate, name='what_rate'),
    path('ajax/', views.ajax, name='ajax'),
]