from django.shortcuts import render,get_object_or_404, redirect
from .models import *
# Create your views here.
def buspost(request):
    return render(request, 'employermodule/buspost.html')


def add_bus_details(request):
    if request.method=='POST':
        bus_name = request.POST.get('bus_name')
        ticket_cost=request.POST.get('ticket_cost')
        bus_type = request.POST.get('bus_type')
        noofseats = request.POST.get('noofseats')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        provisions = request.POST.get('provisions')


        bus_details=BusDetails(
            bus_name=bus_name,
            ticket_cost=ticket_cost,
            bus_type=bus_type,
            noofseats=noofseats,
            pickup=pickup,
            destination=destination,
            provisions=provisions,
        )
        bus_details.save()
        return render(request, 'employermodule/datainserted.html')
    return render(request,'employerhomepage.html')



def view_bus_details(request):
    bus_details_list = BusDetails.objects.all()
    #bus_details_list_as_list = list(bus_details_list)
    return render(request, 'employermodule/view_bus_details.html', {'bus_details_list': bus_details_list})

def edit_bus_details(request, bus_id):
    bus_details = get_object_or_404(BusDetails, id=bus_id)
    if request.method == 'POST':
        bus_details.bus_name = request.POST.get('bus_name')
        bus_details.ticket_cost = request.POST.get('ticket_cost')
        bus_details.bus_type = request.POST.get('bus_type')
        bus_details.noofseats = request.POST.get('noofseats')
        bus_details.pickup = request.POST.get('pickup')
        bus_details.destination = request.POST.get('destination')
        bus_details.provisions = request.POST.get('provisions')
        bus_details.save()
        return redirect('employermodule:view_bus_details')
    return render(request,'employermodule/edit_bus_details.html', {'bus_details':bus_details})



