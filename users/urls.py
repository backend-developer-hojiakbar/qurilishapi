from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('devices/', views.device_list_view, name='device_list'),
    path('devices/register/', views.register_device_view, name='register_device'),
    path('devices/remove/<str:device_id>/', views.remove_device_view, name='remove_device'),
]