from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Dvd(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the DVD")
    borrower = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a DVD.
        """
        return reverse('rental-dvd-detail', args=[str(self.id)])

    @property
    def short_summary(self):
        if self.summary:
            return self.summary[:50] + (self.summary[75:] and '...')
        return ''

    @property
    def is_available(self):
        if self.borrower_id:
            return False
        return True

    @property
    def renter_name(self):
        if self.borrower:
            return self.borrower.username
        return ''

    @property
    def renter_id(self):
        return self.borrower_id
