from rest_framework import generics, permissions, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import ValidationError
import logging
from .models import WaitlistUser, PartnerVenue
from .serializers import WaitlistUserSerializer, PartnerVenueSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

class WaitlistUserViewSet(viewsets.ModelViewSet):
    queryset = WaitlistUser.objects.all()
    serializer_class = WaitlistUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({
                    'message': 'Registration successful',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'error': 'Invalid data provided',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Registration failed: {str(e)}")
            return Response({
                'error': 'Registration failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': 'Failed to fetch waitlist data', 'detail': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class PartnerVenueViewSet(viewsets.ModelViewSet):
    queryset = PartnerVenue.objects.all()
    serializer_class = PartnerVenueSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({
                    'message': 'Venue registered successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'error': 'Invalid data provided',
                'details': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Venue registration failed: {str(e)}")
            return Response({
                'error': 'Venue registration failed',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'message': 'Venues retrieved successfully',
                'data': serializer.data
            })
        except Exception as e:
            logger.error(f"Failed to fetch venues: {str(e)}")
            return Response({
                'error': 'Failed to fetch venue data',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WaitlistUserListView(generics.ListAPIView):
    queryset = WaitlistUser.objects.all()
    serializer_class = WaitlistUserSerializer
    permission_classes = [AllowAny]  # Changed from IsAuthenticated to AllowAny

    @swagger_auto_schema(
        operation_description="Get list of all waitlist users (Public access)",
        responses={
            200: openapi.Response(
                description="List of waitlist users",
                schema=WaitlistUserSerializer(many=True)
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PartnerVenueListView(generics.ListAPIView):
    queryset = PartnerVenue.objects.all()
    serializer_class = PartnerVenueSerializer
    permission_classes = [AllowAny]  # Changed from IsAuthenticated to AllowAny

    @swagger_auto_schema(
        operation_description="Get list of all partner venues (Public access)",
        responses={
            200: openapi.Response(
                description="List of partner venues",
                schema=PartnerVenueSerializer(many=True)
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

