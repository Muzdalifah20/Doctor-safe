from django.db import models
from django.contrib.auth.models import AbstractUser
 

class CustomUser(AbstractUser):
    """
    CustomUser extends the built-in AbstractUser to add a profile picture field.
    This model represents the user with an optional profile image.
    """
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
   

    def __str__(self):
        return self.username