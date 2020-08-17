from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from . import serializers, models
from rest_framework.response import Response



# Create your views here.

class ContactUs(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        contactus = models.ContactUs.objects.all()
        if pk!=None:
            contactus = self.get_object(pk)
        serializer = serializers.ContactUsSerializer(contactus, many=True)
        return Response({"ContactUs": serializer.data})

    def post(self, request, format=None):
        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return models.ContactUs.objects.get(pk=pk)
        except models.ContactUs.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        contactus = self.get_object(pk)
        contactus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

