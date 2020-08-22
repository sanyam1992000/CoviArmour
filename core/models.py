from django.db import models

# Create your models here.
membership = (
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Platinum', 'Platinum'),
)

type_of_firm = (
    ('Individual', 'Individual'),
    ('Private Firm', 'Private'),
    ('Government Firm', 'Government'),
)


class ContactUs(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1000, default=None)
    email = models.EmailField(blank=True, null=True)
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=1000, default=None)
    message = models.TextField()

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return str(self.name) + str(self.subject)


class Enquiry(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=type_of_firm, default='Private' , max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.PositiveIntegerField()
    membership = models.CharField(choices=membership, default='Silver', max_length=100, blank=True, null=True)

    subject = models.CharField(max_length=1000, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return str(self.name) + str(self.subject)


class Franchise(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    name_of_firm = models.CharField(max_length=1000, default=None)
    name_of_contact_person = models.CharField(max_length=1000, default=None)
    email = models.EmailField(blank=True, null=True)
    phone = models.BigIntegerField(default=None)

    address = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    membership = models.CharField(choices=membership, max_length=100, default='Silver')

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Franchise'
        verbose_name_plural = 'Franchises'

    def __str__(self):
        return str(self.name_of_firm) + str(self.city)

