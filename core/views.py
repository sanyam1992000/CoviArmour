from django.http.response import Http404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status, viewsets
from django.core.mail import send_mail, EmailMessage

from django.conf import settings
from . import serializers, models, forms, tasks
from rest_framework.response import Response

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = forms.ContactUsForm(request.POST)
        form1 = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']

            subject = 'New Query on Website for CoviArmour'
            message = 'Dear {}, \nWe received a query from your behalf,\n Subject : {}\n \nMessage : {}\nWe will contact you on {}'.format(name, subject, message, phone)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['sanyam30dav@gmail.com', str(email)]
            tasks.send_email(subject, message, from_email, to_email)
            print("###################################")

            # messages.success(request, 'We will Contact you soon!')
            return redirect('core:contact')

        if form1.is_valid():
            form1.save()
            return redirect('core:home')

        # else:
        #     messages.error(request, 'invalid input')
    else:
        form = forms.ContactUsForm()
        form1 = forms.EnquiryForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'contact.html', context=context)

def franchise(request):
    if request.method == 'POST':
        form = forms.FranchiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = forms.FranchiseForm()
    return render(request, 'franchise.html', {'form': form})

def services(request):
    return render(request, 'services.html')

class ContactUsAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        contactus = models.ContactUs.objects.all()
        if pk!=None:
            contactus = self.get_object(pk)
        serializer = serializers.ContactUsSerializer(contactus, many=True)
        return Response({"ContactUs": serializer.data}, status=status.HTTP_200_OK)

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


class EnquiryAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        object = models.Enquiry.objects.all()
        if pk!=None:
            object = self.get_object(pk)
        serializer = serializers.EnquirySerializer(object, many=True)
        return Response({"ContactUs": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return models.Enquiry.objects.get(pk=pk)
        except models.Enquiry.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Franchise(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        object = models.Franchise.objects.all()
        if pk!=None:
            object = self.get_object(pk)
        serializer = serializers.FranchiseSerializer(object, many=True)
        return Response({"ContactUs": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = serializers.FranchiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return models.Franchise.objects.get(pk=pk)
        except models.Franchise.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
    permission_classes = [permissions.AllowAny]


class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = models.Enquiry.objects.all()
    serializer_class = serializers.EnquirySerializer
    permission_classes = [permissions.AllowAny]


class FranchiseViewSet(viewsets.ModelViewSet):
    queryset = models.Franchise.objects.all()
    serializer_class = serializers.FranchiseSerializer
    permission_classes = [permissions.AllowAny]


def handler404(request, exception):
    return render(request, '404.html', status=404)

#
# def handler500(request):
#     return render(request, '500.html', status=500)
#
#
# def handler403(request,exception):
#     return render(request, '403.html', status=403)
#
#
# def handler400(request,exception):
#     return render(request, '400.html', status=400)