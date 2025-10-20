from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctor")
    pricing_info = models.TextField()
    safety_rating = models.DecimalField(max_digits=3, decimal_places=2)
    verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    contact_info = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name[:50]
    