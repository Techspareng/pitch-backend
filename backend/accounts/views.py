from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from fitaccess.models import WaitlistUser, PartnerVenue
from fitaccess.serializers import WaitlistUserSerializer, PartnerVenueSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

class AdminWaitlistView(generics.ListCreateAPIView):
    queryset = WaitlistUser.objects.all()
    serializer_class = WaitlistUserSerializer
    permission_classes = [AllowAny]  # Changed to AllowAny

    def get(self, request, *args, **kwargs):
        try:
            waitlist_users = self.get_queryset()
            serializer = self.get_serializer(waitlist_users, many=True)
            return Response({
                'count': waitlist_users.count(),
                'results': serializer.data
            })
        except Exception as e:
            return Response(
                {'error': 'Failed to fetch waitlist data', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Registration successful',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'error': 'Invalid data provided',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': 'Registration failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminPartnerView(generics.ListCreateAPIView):
    queryset = PartnerVenue.objects.all()
    serializer_class = PartnerVenueSerializer
    permission_classes = [AllowAny]  # Changed to AllowAny

    def get(self, request, *args, **kwargs):
        try:
            partners = self.get_queryset()
            serializer = self.get_serializer(partners, many=True)
            return Response({
                'count': partners.count(),
                'results': serializer.data
            })
        except Exception as e:
            return Response(
                {'error': 'Failed to fetch partner data', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Venue registered successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'error': 'Invalid data provided',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': 'Venue registration failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)