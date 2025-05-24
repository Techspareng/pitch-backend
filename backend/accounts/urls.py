from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    UserListView,
    UserViewSet,
    AdminWaitlistView,
    AdminPartnerView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  # Added login endpoint
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Added token refresh
    path('users/', UserListView.as_view(), name='user-list'),
    path('me/', UserViewSet.as_view({'get': 'me'}), name='user-me'),
    path('admin/waitlist/', AdminWaitlistView.as_view(), name='admin-waitlist'),
    path('admin/partners/', AdminPartnerView.as_view(), name='admin-partners'),
]