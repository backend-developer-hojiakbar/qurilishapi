from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Convert empty string to None for phone_number to avoid UNIQUE constraint issues
        if self.phone_number == '':
            self.phone_number = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username or self.email or f"User-{self.pk}"


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'device_id')

    def __str__(self):
        return f"{self.user} - {self.device_id}"