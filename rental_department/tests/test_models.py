from django.test import TestCase
from rental_department.models import Dvd
from django.contrib.auth.models import User


class DvdTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test-user")
        Dvd.objects.create(title="title-1")
        Dvd.objects.create(
            title="title-2",
            borrower=user,
            summary='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vulputate ipsum sit amet quam aliquet.'
        )

    def test_get_absolute_url(self):
        dvd1 = Dvd.objects.get(title="title-1")
        self.assertEqual(dvd1.get_absolute_url(), '/rental/dvd/1')

    def test_short_summary(self):
        dvd2 = Dvd.objects.get(title="title-2")
        self.assertEqual(dvd2.short_summary, 'Lorem ipsum dolor sit amet, consectetur adipiscing...')

    def test_is_available(self):
        dvd1 = Dvd.objects.get(title="title-1")
        dvd2 = Dvd.objects.get(title="title-2")
        self.assertTrue(dvd1.is_available)
        self.assertFalse(dvd2.is_available)

    def test_renter_name(self):
        dvd2 = Dvd.objects.get(title="title-2")
        self.assertEqual(dvd2.renter_name, 'test-user')

    def test_renter_id(self):
        dvd2 = Dvd.objects.get(title="title-2")
        user = User.objects.get(username='test-user')
        self.assertEqual(dvd2.renter_id, user.id)


