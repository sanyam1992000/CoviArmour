from django.db import models

# Create your models here.

class ContactUs(models.Model):
    datetime = models.DateTimeField()
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return str(self.name) + str(self.subject)


class Enquiry(models.Model):
    datetime = models.DateTimeField()
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField()
    pincode = models.PositiveIntegerField()
    membership = models.CharField(blank=True, null=True)

    subject = models.CharField(max_length=1000)
    message = models.TextField()

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return str(self.name) + str(self.subject)


class Franchise(models.Model):
    datetime = models.DateTimeField()
    name_of_firm = models.CharField(max_length=1000)
    name_of_contact_person = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField()
    pincode = models.PositiveIntegerField()
    membership = models.CharField(blank=True, null=True)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return str(self.name_of_firm) + str(self.city)

