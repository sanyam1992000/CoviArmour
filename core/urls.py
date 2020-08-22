from django.urls import path, include
from . import views as coreviews
app_name = 'core'

urlpatterns = [
    path('', coreviews.home, name='home'),
    path('about/', coreviews.about, name='about'),
    path('technology/', coreviews.about, name='technology'),
    path('services/', coreviews.services, name='services'),
    path('franchise/', coreviews.franchise, name='franchise'),
    path('certification/', coreviews.about, name='certification'),
    path('contact/', coreviews.contact, name='contact'),
]


