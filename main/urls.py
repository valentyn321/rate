from django.urls import path
from . import views

urlpatterns = [
    path('', views.currenties_list, name='currenties_list'),
]