from django.test import TestCase
from restaurant.models import Menu 

class MenuTest(TestCase):
    def text_get_item(self):
        item = Menu.objects.create(name="IceCream", price=5, menu_item_description="Mango IceCream")
        self.assertEqual(item, "IceCream")
        