from django.db import models
from django.utils import timezone
from users.models import User


class CaseFile(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    extracted_text = models.TextField(blank=True, null=True)
    document_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class CaseParticipant(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Task(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")


class TimelineEvent(models.Model):
    date = models.DateTimeField()
    description = models.TextField()
    event_type = models.CharField(max_length=20, default='event')  # 'event' or 'deadline'
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description[:50] + ("..." if len(self.description) > 50 else "")


class EvidenceItem(models.Model):
    file_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    evidence_type = models.CharField(max_length=100)
    ai_summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class BillingEntry(models.Model):
    date = models.DateTimeField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.description[:50]}... ({self.hours} hours)"


class Note(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:50] + ("..." if len(self.content) > 50 else "")


class KnowledgeBaseSection(models.Model):
    key_facts = models.JSONField(default=list)  # List of {fact, relevance}
    legal_issues = models.JSONField(default=list)  # List of strings
    applicable_laws = models.JSONField(default=list)  # List of {article, summary, url}
    strengths = models.JSONField(default=list)  # List of strings
    weaknesses = models.JSONField(default=list)  # List of strings
    statute_of_limitations_status = models.CharField(max_length=20, default='OK')  # 'OK', 'Muddati o'tgan', 'Xavf ostida'
    statute_of_limitations_summary = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Knowledge Base Section {self.id}"


class RiskMatrixEntry(models.Model):
    risk = models.TextField()
    likelihood = models.CharField(max_length=10)  # 'Past', 'O'rta', 'Yuqori'
    mitigation = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.risk[:50] + ("..." if len(self.risk) > 50 else "")


class DebateResult(models.Model):
    summary = models.TextField()
    win_probability = models.IntegerField()
    probability_justification = models.TextField()
    positive_factors = models.JSONField(default=list)  # List of strings
    negative_factors = models.JSONField(default=list)  # List of strings
    suggested_tasks = models.JSONField(default=list)  # List of strings
    deep_dive_analysis = models.TextField(blank=True, null=True)
    courtroom_scenario = models.TextField(blank=True, null=True)
    cross_examination_questions = models.JSONField(default=list)  # List of {question, suggestedAnswer}
    closing_argument_lead = models.TextField(blank=True, null=True)
    closing_argument_defender = models.TextField(blank=True, null=True)
    client_summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Debate Result (Win Probability: {self.win_probability}%)"


class Case(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')
    title = models.CharField(max_length=255)
    case_details = models.TextField()
    court_stage = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100)
    client_name = models.CharField(max_length=255)
    tags = models.JSONField(default=list)  # List of strings
    folder = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    files = models.ManyToManyField(CaseFile, blank=True, related_name='cases')
    participants = models.ManyToManyField(CaseParticipant, blank=True, related_name='cases')
    tasks = models.ManyToManyField(Task, blank=True, related_name='cases')
    timeline = models.ManyToManyField(TimelineEvent, blank=True, related_name='cases')
    evidence = models.ManyToManyField(EvidenceItem, blank=True, related_name='cases')
    billing = models.ManyToManyField(BillingEntry, blank=True, related_name='cases')
    notes = models.ManyToManyField(Note, blank=True, related_name='cases')
    knowledge_base = models.OneToOneField(KnowledgeBaseSection, on_delete=models.CASCADE, blank=True, null=True)
    risk_matrix = models.ManyToManyField(RiskMatrixEntry, blank=True, related_name='cases')
    debate_result = models.OneToOneField(DebateResult, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title