from django.shortcuts import render

# Create your views here.
def viewbusses(request):
    return render(request, 'customermodule/viewbusses.html')

from employermodule.models import BusDetails
def bus_details_list(request):
    bus_details_list=BusDetails.objects.all()
    return render(request,'customermodule/viewbusses.html', {'bus_details_list': bus_details_list})


