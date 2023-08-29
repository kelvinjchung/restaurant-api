from django.test import TestCase
from reservation.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=5, inventory=20)
        self.assertEqual(str(item), "Ice Cream : 5")
