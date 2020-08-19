from rest_framework import serializers
from . import models


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactUs
        fields = "__all__"


class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Enquiry
        fields = "__all__"


class FranchiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Franchise
        fields = "__all__"