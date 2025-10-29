from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Device


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'full_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'full_name')

    def validate_phone_number(self, value):
        """
        Check that the phone number is unique, but allow the current user to keep their own phone number.
        Also convert empty strings to None to avoid UNIQUE constraint issues.
        """
        if value == '':
            value = None
            
        if value:
            user = self.instance
            if user and User.objects.filter(phone_number=value).exclude(pk=user.pk).exists():
                raise serializers.ValidationError("This phone number is already in use.")
        return value


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'device_id', 'name', 'last_login', 'is_active', 'created_at')
        read_only_fields = ('id', 'last_login', 'created_at')


class LoginSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=20)
    phone_number = serializers.CharField(max_length=15, required=False)

    def validate(self, attrs):
        token = attrs.get('token')
        # In a real implementation, you would validate the token against your system
        # For now, we'll just check if it's not empty
        if not token:
            raise serializers.ValidationError('Token is required')
        return attrs


class RegisterDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'name')

    def validate_device_id(self, value):
        if not value:
            raise serializers.ValidationError('Device ID is required')
        return value