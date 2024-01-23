from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default="")

    def __str__(self):
        return self.name 
    

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=2)

    def __str__(self):
        return self.first_name 
    
