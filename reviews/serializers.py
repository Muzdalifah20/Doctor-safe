from rest_framework import serializers
from .models import Review
from doctors.models import Doctor
class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review model.
    The user field is read-only and represented as string.
    """
    user = serializers.StringRelatedField(read_only=True)
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        """
        Override create method to associate the review with the request user.
        """
        model = Review
        fields = ['id', 'user', 'doctor', 'rating', 'comment', 'timestamp']
        read_only_fields = ['id', 'user', 'doctor', 'timestamp']

    