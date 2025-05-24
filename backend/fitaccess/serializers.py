from rest_framework import serializers
from .models import WaitlistUser, PartnerVenue

class WaitlistUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistUser
        fields = ['id', 'name', 'email', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        return WaitlistUser.objects.create(**validated_data)

class PartnerVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerVenue
        fields = [
            'id',
            'name',
            'venueName',
            'description',
            'email',
            'phone',
            'venueType',
            'location',
            'address',
            'city',
            'website',
            'facilities',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']