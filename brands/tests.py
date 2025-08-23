from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from brands.models import Brand, Owner

class BrandListViewTest(APITestCase):
    def setUp(self):
        owner = Owner.objects.create(name="Juan Navarrete")
        Brand.objects.create(name="Marca 1", owner=owner)
        Brand.objects.create(name="Marca 2", owner=owner)

    def test_list_all_brands(self):
        url = reverse('brand-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)
        self.assertEqual(response.data["data"][0]["owner"]["name"], "Juan Navarrete")
