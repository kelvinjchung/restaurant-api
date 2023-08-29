from django.test import TestCase
from reservation.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Ice Cream", price=5, inventory=20)
        self.item2 = Menu.objects.create(title="Cake", price=40, inventory=3)
        self.item3 = Menu.objects.create(title="Apple Pie", price=12, inventory=10)

    def test_get_all(self):
        response = self.client.get("/restaurant/menu")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        for i in range(3):
            self.assertEqual(
                response.data[i]["id"],
                [self.item1.id, self.item2.id, self.item3.id][i],
            )
            self.assertEqual(
                response.data[i]["title"], ["Ice Cream", "Cake", "Apple Pie"][i]
            )
            self.assertEqual(response.data[i]["price"], ["5.00", "40.00", "12.00"][i])
            self.assertEqual(response.data[i]["inventory"], [20, 3, 10][i])
