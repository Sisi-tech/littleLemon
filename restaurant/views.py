from django.shortcuts import render
from django.http import HttpResponse 
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from datetime import datetime 
import json 

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    menu_serializer = MenuSerializer(menu_data, many=True)
    serialized_menu = menu_serializer.data
    main_data = {"menu": serialized_menu}
    return render(request, "menu.html", {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if not exist:
            booking = Booking(
                first_name = data['first_name'],
                reservation_data = data['reservation_date'],
                reservation_slot = data['reservation_slot'],
            )
            bookings.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date', datetime.today().date())
    bookings_queryset = Booking.objects.all()
    booking_serializer = BookingSerializer(bookings_queryset, many=True)
    serialized_bookings = booking_serializer.data 
    return render(request, 'bookings.html', {'bookings': serialized_bookings})
