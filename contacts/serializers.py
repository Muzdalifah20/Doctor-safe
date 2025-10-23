from rest_framework import serializers
from .models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for ContactRequest model.
    User field is read-only and represented as a string.
    Status is read-only to enforce controlled updates.
    """
    user = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = ContactRequest
        fields = ['id', 'user', 'doctor_name', 'request_details', 'status', 'timestamp']
        read_only_fields = ['id', 'user', 'status', 'timestamp']

     