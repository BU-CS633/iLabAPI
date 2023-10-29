from django.test import TestCase
from django.urls import reverse
from .models import Item, Status, Request
from django.contrib.auth.models import User


# python manage.py test --keepdb


class ItemDetailViewTestCase(TestCase):
    def setUp(self):
        # Create a sample item
        self.item = Item.objects.create(
            name="Test Item",
            qty=10,
            vendor="Test Vendor",
            catalog="Test Catalog",
            lastOrderDate="2022-01-01",
            lastReceivedDate="2022-01-10"
        )

    def test_existing_item(self):
        # Generate the URL for the view using the reverse function
        url = reverse('item_detail', args=[self.item.id])

        # Test that the view returns correct data for an existing item
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        expected_data = {
            "id": self.item.id,
            "name": "Test Item",
            "qty": 10,
            "vendor": "Test Vendor",
            "catalog": "Test Catalog",
            "lastOrderDate": "2022-01-01",
            "lastReceivedDate": "2022-01-10"
        }

        self.assertEqual(response.json(), expected_data)

    def test_non_existing_item(self):
        # Generate the URL for the view using the reverse function
        url = reverse('item_detail', args=[99999])

        # Test that the view raises a 404 status for a non-existing item
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class ApproveRequestTest(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.status_pending = Status.objects.create(description='pending')
        self.status_approved = Status.objects.create(description='approved')
        self.item = Item.objects.create(name='Item1', qty=10)
        self.request = Request.objects.create(
            item=self.item,
            status=self.status_pending,
            owner=self.user,
        )

    def test_approve_request(self):
        # print(f"updated_request.status: {self.request.status}")
        response = self.client.get(reverse('approve_request', args=[self.request.id]))
        # Fetch the updated inventory request from the database
        updated_request = Request.objects.get(pk=self.request.id)
        # print(f"updated_request.status: {updated_request.status}")
        # print(f"self.status_approved: {self.status_approved}")
        # Check that the status is updated to "approved"
        self.assertEqual(updated_request.status, self.status_approved)

        # Check that the approved_date is set to the current date
        self.assertIsNotNone(updated_request.approved_date)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response data is correct
        self.assertEqual(response.json(), {'message': 'Request approved successfully!'})
