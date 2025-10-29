from rest_framework import serializers
from .models import (
    Case, CaseFile, CaseParticipant, Task, TimelineEvent, 
    EvidenceItem, BillingEntry, Note, KnowledgeBaseSection, 
    RiskMatrixEntry, DebateResult
)


class CaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseFile
        fields = '__all__'


class CaseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseParticipant
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineEvent
        fields = '__all__'


class EvidenceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvidenceItem
        fields = '__all__'


class BillingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingEntry
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class KnowledgeBaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBaseSection
        fields = '__all__'


class RiskMatrixEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskMatrixEntry
        fields = '__all__'


class DebateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateResult
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    files = CaseFileSerializer(many=True, read_only=True)
    participants = CaseParticipantSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    timeline = TimelineEventSerializer(many=True, read_only=True)
    evidence = EvidenceItemSerializer(many=True, read_only=True)
    billing = BillingEntrySerializer(many=True, read_only=True)
    notes = NoteSerializer(many=True, read_only=True)
    knowledge_base = KnowledgeBaseSectionSerializer(read_only=True)
    risk_matrix = RiskMatrixEntrySerializer(many=True, read_only=True)
    debate_result = DebateResultSerializer(read_only=True)

    class Meta:
        model = Case
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class CaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            'id', 'title', 'case_details', 'court_stage', 
            'client_role', 'client_name', 'tags', 'folder', 'timestamp'
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            'title', 'case_details', 'court_stage', 
            'client_role', 'client_name', 'tags', 'folder', 'timestamp'
        )