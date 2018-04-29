from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rental_department.models import Dvd
from django.contrib.auth.models import User


class StorefrontTest(TestCase):
    def setUp(self):
        self.dvd1 = Dvd.objects.create(title="title-1")
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.dvd2 = Dvd.objects.create(title="title-2")
        self.client = Client()

        self.client.login(username='temporary', password='temporary')

        self.dvd2.borrower = self.user
        self.dvd2.save()

    def test_main(self):
        response = self.client.get(reverse('rental'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['num_dvd'], 2)

    def test_dvd_list(self):
        response = self.client.get(reverse('rental-dvd-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['dvd_list']), 2)

    def test_dvd_detail(self):
        response = self.client.get(reverse('rental-dvd-detail', args=[str(self.dvd1.id)]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['dvd'].id, self.dvd1.id)

    def test_rent_dvd(self):
        self.client.get(reverse('rent-dvd', args=[str(self.dvd1.id)]))

        updated_dvd1 = Dvd.objects.get(title="title-1")
        self.assertEqual(updated_dvd1.borrower_id, self.user.id)

    def test_return_dvd(self):
        self.client.get(reverse('return-dvd', args=[str(self.dvd2.id)]))

        updated_dvd2 = Dvd.objects.get(title="title-2")
        self.assertIsNone(updated_dvd2.borrower_id)

    def test_my_dvd(self):
        response = self.client.get(reverse('my-dvd'))
        dvd_list = response.context['list']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(dvd_list), 1)
        self.assertEqual(dvd_list[0].id, self.dvd2.id)
