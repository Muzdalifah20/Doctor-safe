from django.db import models
from django.conf import settings

class ContactRequest(models.Model):
    """
    Model representing a contact request sent by a user to a doctor.
    Tracks request details and approval status.
    """
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
        """
        String representation showing the user, doctor name and request status.
        """

        return f'ContactRequest from {self.user} to {self.doctor_name} - {self.status}'
