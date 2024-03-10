from django.contrib import admin
from django.urls import path, include
from . import views

app_name='employermodule'
urlpatterns = [
    path('buspost/',views.buspost,name='buspost'),
    path('add_bus_details',views.add_bus_details,name='add_bus_details'),
    path('view',views.view_bus_details,name='view_bus_details'),
    path('edit/<int:bus_id>/',views.edit_bus_details,name='edit_bus_details'),
]