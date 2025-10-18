from rest_framework import serializers
from .models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = ContactRequest
        fields = ['id', 'user', 'doctor_name', 'request_details', 'status', 'timestamp']
        read_only_fields = ['id', 'user', 'status', 'timestamp']

    def create(self, validated_data):
        user = self.context['request'].user
        return ContactRequest.objects.create(user=user, **validated_data)
