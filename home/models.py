from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=7)
    phone_number = models.CharField(unique=True)
    country = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.country_code} {self.phone_number}'

    class Meta:
        unique_together = (('first_name', 'last_name'),)
