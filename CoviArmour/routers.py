from rest_framework.routers import DefaultRouter
from core import views as coreviews

router = DefaultRouter()
router.register('contactus', coreviews.ContactUsViewSet, basename='ContactUs')
router.register('enquiries', coreviews.EnquiryViewSet, basename='Enquiry')
router.register('franchise', coreviews.FranchiseViewSet, basename='Franchise')
