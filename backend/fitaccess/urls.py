from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaitlistUserViewSet, PartnerVenueViewSet

router = DefaultRouter()
router.register(r'waitlist', WaitlistUserViewSet)
router.register(r'venues', PartnerVenueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]