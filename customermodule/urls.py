from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('viewbusses',views.viewbusses,name='viewbusses'),
    path('bus_details_list',views.bus_details_list,name='bus_details_list'),
]