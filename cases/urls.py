from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list_view, name='case_list'),
    path('create/', views.case_create_view, name='case_create'),
    path('<str:case_id>/', views.case_detail_view, name='case_detail'),
    path('<str:case_id>/update/', views.case_update_view, name='case_update'),
    path('<str:case_id>/delete/', views.case_delete_view, name='case_delete'),
    
    # Case Files
    path('<str:case_id>/files/add/', views.add_case_file_view, name='add_case_file'),
    path('<str:case_id>/files/upload/', views.upload_case_file_view, name='upload_case_file'),
    
    # Case Participants
    path('<str:case_id>/participants/add/', views.add_case_participant_view, name='add_case_participant'),
    
    # Tasks
    path('<str:case_id>/tasks/add/', views.add_task_view, name='add_task'),
    path('<str:case_id>/tasks/<str:task_id>/update/', views.update_task_view, name='update_task'),
    
    # Timeline Events
    path('<str:case_id>/timeline/add/', views.add_timeline_event_view, name='add_timeline_event'),
    
    # Evidence Items
    path('<str:case_id>/evidence/add/', views.add_evidence_view, name='add_evidence'),
    
    # Billing Entries
    path('<str:case_id>/billing/add/', views.add_billing_entry_view, name='add_billing_entry'),
    
    # Notes
    path('<str:case_id>/notes/add/', views.add_note_view, name='add_note'),
]