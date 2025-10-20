from rest_framework import serializers
from .models import Department, Doctor

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class DoctorSerializer(serializers.ModelSerializer):
    specialization = DepartmentSerializer(read_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source="specialization", write_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'specialization_id', 'pricing_info', 'safety_rating', 'verified', 'bio', 'contact_info', 'image']