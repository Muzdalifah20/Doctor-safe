from django.db import models
from django.conf import settings
from doctors.models import Doctor
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    """
    Model representing a user's review for a doctor with rating and comment.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation displaying user, doctor, and rating.
        """
        return f'Review by {self.user} for {self.doctor} - {self.rating}'
