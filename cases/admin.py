from django.contrib import admin
from .models import (
    Case, CaseFile, CaseParticipant, Task, TimelineEvent, 
    EvidenceItem, BillingEntry, Note, KnowledgeBaseSection, 
    RiskMatrixEntry, DebateResult
)


class CaseFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_type', 'document_type', 'created_at')
    search_fields = ('name', 'file_type', 'document_type')
    readonly_fields = ('created_at',)


class CaseParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    search_fields = ('name', 'role')
    readonly_fields = ('created_at',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('text',)
    readonly_fields = ('created_at', 'updated_at')


class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'event_type', 'created_at')
    list_filter = ('event_type', 'date', 'created_at')
    search_fields = ('description',)
    readonly_fields = ('created_at',)


class EvidenceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'evidence_type', 'timestamp', 'created_at')
    list_filter = ('evidence_type', 'timestamp', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)


class BillingEntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'hours', 'description', 'rate', 'created_at')
    list_filter = ('date', 'created_at')
    search_fields = ('description',)
    readonly_fields = ('created_at',)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp', 'created_at')
    list_filter = ('timestamp', 'created_at')
    search_fields = ('content',)
    readonly_fields = ('created_at',)


class KnowledgeBaseSectionAdmin(admin.ModelAdmin):
    list_display = ('statute_of_limitations_status', 'created_at')
    list_filter = ('statute_of_limitations_status', 'created_at')
    readonly_fields = ('created_at',)


class RiskMatrixEntryAdmin(admin.ModelAdmin):
    list_display = ('risk', 'likelihood', 'mitigation', 'created_at')
    list_filter = ('likelihood', 'created_at')
    search_fields = ('risk', 'mitigation')
    readonly_fields = ('created_at',)


class DebateResultAdmin(admin.ModelAdmin):
    list_display = ('win_probability', 'summary', 'created_at')
    list_filter = ('win_probability', 'created_at')
    search_fields = ('summary',)
    readonly_fields = ('created_at',)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'court_stage', 'client_name', 'timestamp', 'created_at')
    list_filter = ('court_stage', 'timestamp', 'created_at')
    search_fields = ('title', 'case_details', 'client_name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('files', 'participants', 'tasks', 'timeline', 'evidence', 'billing', 'notes', 'risk_matrix')


admin.site.register(CaseFile, CaseFileAdmin)
admin.site.register(CaseParticipant, CaseParticipantAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TimelineEvent, TimelineEventAdmin)
admin.site.register(EvidenceItem, EvidenceItemAdmin)
admin.site.register(BillingEntry, BillingEntryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(KnowledgeBaseSection, KnowledgeBaseSectionAdmin)
admin.site.register(RiskMatrixEntry, RiskMatrixEntryAdmin)
admin.site.register(DebateResult, DebateResultAdmin)
admin.site.register(Case, CaseAdmin)