from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Device
from .serializers import UserSerializer, UserUpdateSerializer, DeviceSerializer, LoginSerializer, RegisterDeviceSerializer
import uuid


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        
        # In a real implementation, you would validate the token against your system
        # For demonstration, we'll accept any non-empty token
        if token:
            # Create or get user
            user, created = User.objects.get_or_create(
                username=f"user_{uuid.uuid4().hex[:8]}",
                defaults={
                    'email': f"user_{uuid.uuid4().hex[:8]}@example.com"
                }
            )
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_view(request):
    serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def device_list_view(request):
    devices = Device.objects.filter(user=request.user)
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_device_view(request):
    serializer = RegisterDeviceSerializer(data=request.data)
    if serializer.is_valid():
        device_id = serializer.validated_data['device_id']
        
        # Check if user already has 2 devices
        user_devices_count = Device.objects.filter(user=request.user, is_active=True).count()
        if user_devices_count >= 2:
            return Response(
                {'error': 'Maximum device limit (2) reached. Please remove a device first.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create or get device
        device, created = Device.objects.get_or_create(
            user=request.user,
            device_id=device_id,
            defaults={
                'name': serializer.validated_data.get('name', 'Unknown Device'),
                'is_active': True
            }
        )
        
        if not created:
            # Update existing device
            device.name = serializer.validated_data.get('name', device.name)
            device.is_active = True
            device.save()
        
        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_device_view(request, device_id):
    try:
        device = Device.objects.get(user=request.user, device_id=device_id)
        device.delete()
        return Response({'message': 'Device removed successfully'}, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)