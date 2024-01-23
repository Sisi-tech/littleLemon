from django.test import TestCase
from restaurant.views import Menu 

class MenuViewTest(TestCast):
    def setup(self):
        self.setup(Menu)
    def test_getall(self):
        item = Menu.objects.all()
        self.assertEqual(item)
