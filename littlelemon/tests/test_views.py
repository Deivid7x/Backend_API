from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=120, Inventory=50)

    def test_getall(self):
        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)
        serialized_data = serializer.data

        expected_data = [
            {'id': 1, 'Title': 'IceCream', 'Price': 80, 'Inventory': 100},
            {'id': 2, 'Title': 'Pizza', 'Price': 120, 'Inventory': 50}
        ]
        self.assertEqual(serialized_data, expected_data)
