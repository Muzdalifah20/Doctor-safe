from django.db import models
from django.conf import settings

class ContactRequest(models.Model):

    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contact_requests')
    doctor_name = models.CharField(max_length=255)
    request_details = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'ContactRequest from {self.user} to {self.doctor_name} - {self.status}'
