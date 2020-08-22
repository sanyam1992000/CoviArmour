from django import forms
from . import models


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = '__all__'


class FranchiseForm(forms.ModelForm):
    class Meta:
        model = models.Franchise
        fields = '__all__'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.Enquiry
        fields = '__all__'
