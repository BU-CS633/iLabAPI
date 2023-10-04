from django.test import TestCase, Client
from .models import Item


class ItemDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a sample item
        self.item = Item.objects.create(
            name="Test Item",
            vendor="Test Vendor",
            catalog="Test Catalog",
            lastOrderDate="2022-01-01",
            lastReceivedDate="2022-01-10"
        )

    def test_existing_item(self):
        # Test that the view returns correct data for an existing item
        response = self.client.get(f'http://127.0.0.1:8000/api/item/1/')

        self.assertEqual(response.status_code, 200)

        expected_data = {
            "id": self.item.id,
            "name": "Test Item",
            "vendor": "Test Vendor",
            "catalog": "Test Catalog",
            "lastOrderDate": "2022-01-01",
            "lastReceivedDate": "2022-01-10"
        }

        self.assertEqual(response.json(), expected_data)

    def test_non_existing_item(self):
        # Test that the view raises a 404 status for a non-existing item
        response = self.client.get('http://127.0.0.1:8000/api/item/99999/')  # Assuming 99999 is a non-existing item id

        self.assertEqual(response.status_code, 404)
