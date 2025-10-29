import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Case, CaseFile, CaseParticipant, Task, TimelineEvent, EvidenceItem, BillingEntry, Note
from .serializers import (
    CaseSerializer, CaseCreateSerializer, CaseUpdateSerializer,
    CaseFileSerializer, CaseParticipantSerializer, TaskSerializer,
    TimelineEventSerializer, EvidenceItemSerializer, BillingEntrySerializer, NoteSerializer
)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def case_list_view(request):
    cases = Case.objects.filter(user=request.user).order_by('-timestamp')
    serializer = CaseSerializer(cases, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def case_create_view(request):
    serializer = CaseCreateSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        case = serializer.save()
        return Response(CaseSerializer(case).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def case_detail_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = CaseSerializer(case)
        return Response(serializer.data)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def case_update_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = CaseUpdateSerializer(case, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(CaseSerializer(case).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def case_delete_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        case.delete()
        return Response({'message': 'Case deleted successfully'}, status=status.HTTP_200_OK)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# Case Files
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_case_file_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = CaseFileSerializer(data=request.data)
        if serializer.is_valid():
            case_file = serializer.save()
            case.files.add(case_file)
            return Response(CaseFileSerializer(case_file).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# New endpoint for file uploads with binary data
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_case_file_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        
        # Get file data from form data
        file_data_json = request.data.get('file_data')
        file = request.FILES.get('file')
        
        if not file_data_json or not file:
            return Response({'error': 'File data and file are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Parse file data
        try:
            file_data = json.loads(file_data_json)
        except json.JSONDecodeError:
            return Response({'error': 'Invalid file data format'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create CaseFile instance
        serializer = CaseFileSerializer(data=file_data)
        if serializer.is_valid():
            case_file = serializer.save()
            case.files.add(case_file)
            
            # For audio files, we might want to store them in the media directory
            # This is a simplified approach - in production, you'd want to save the file
            # and store the path in the database
            
            return Response(CaseFileSerializer(case_file).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Case Participants
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_case_participant_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = CaseParticipantSerializer(data=request.data)
        if serializer.is_valid():
            participant = serializer.save()
            case.participants.add(participant)
            return Response(CaseParticipantSerializer(participant).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# Tasks
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            case.tasks.add(task)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_view(request, case_id, task_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        task = case.tasks.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(TaskSerializer(task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


# Timeline Events
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_timeline_event_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = TimelineEventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            case.timeline.add(event)
            return Response(TimelineEventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# Evidence Items
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_evidence_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = EvidenceItemSerializer(data=request.data)
        if serializer.is_valid():
            evidence = serializer.save()
            case.evidence.add(evidence)
            return Response(EvidenceItemSerializer(evidence).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# Billing Entries
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_billing_entry_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = BillingEntrySerializer(data=request.data)
        if serializer.is_valid():
            billing_entry = serializer.save()
            case.billing.add(billing_entry)
            return Response(BillingEntrySerializer(billing_entry).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)


# Notes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note_view(request, case_id):
    try:
        case = Case.objects.get(id=case_id, user=request.user)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            case.notes.add(note)
            return Response(NoteSerializer(note).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Case.DoesNotExist:
        return Response({'error': 'Case not found'}, status=status.HTTP_404_NOT_FOUND)