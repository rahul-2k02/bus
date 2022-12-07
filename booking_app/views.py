from django.shortcuts import render
from .models import BookingDetails
from django.http import HttpResponseRedirect
from .forms import ContactForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def ticketsView(request):
    all_tickets = BookingDetails.objects.all()
    return render(request, 'tickets.html',  {'all_items': all_tickets})


def addTicketsView(request):
    # x = request.POST.get('todotext')
    new_item = BookingDetails()
    new_item_age = BookingDetails()
    new_item.name = request.POST.get('name')
    new_item.save()
    new_item_age.age = request.POST.get('age')
    new_item_age.save()

    return HttpResponseRedirect('/tickets/')


def book(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            trip_date = form.cleaned_data['trip_date']
            gender = form.cleaned_data['gender']
            dep = form.cleaned_data['dep']
            arr = form.cleaned_data['arr']


            data = {'name': name}
            data['gender'] = gender
            data['trip_date'] = trip_date
            data['dep'] = dep
            data['arr'] = arr


            return render(request, 'final.html', data)
    return render(request, 'booking.html', {'form': form})


def deleteTicketsView(request, i):
    y = BookingDetails.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/tickets/')
