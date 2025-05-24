from django.db import models
from django.core.validators import URLValidator

class WaitlistUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Waitlist User'
        verbose_name_plural = 'Waitlist Users'

    def __str__(self):
        return self.email

class PartnerVenue(models.Model):
    VENUE_TYPES = [
        ('GYM', 'Gym'),
        ('POOL', 'Swimming Pool'),
        ('STUDIO', 'Fitness Studio'),
        ('FIELD', 'Sports Field'),
        ('OTHER', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('PENDING', 'Pending'),
        ('INACTIVE', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    venueName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    venueType = models.CharField(max_length=10, choices=VENUE_TYPES)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True, validators=[URLValidator()])
    facilities = models.JSONField(default=list)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Partner Venue'
        verbose_name_plural = 'Partner Venues'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.venueName}"
