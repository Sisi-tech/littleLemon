from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ['name', 'price', 'menu_item_description']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking 
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        

