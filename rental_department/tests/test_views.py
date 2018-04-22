import unittest
from django.test import Client
from rental_department.models import Dvd


class StorefrontTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        Dvd.objects.create(title="title-1")

    def test_main(self):
        response = self.client.get('/rental/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['num_dvd'], 1)
