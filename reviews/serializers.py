from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'doctor', 'rating', 'comment', 'timestamp']
        read_only_fields = ['id', 'user', 'timestamp']

        def create(self, validated_data):
            user = self.context['request'].user
            return Review.objects.create(user=user, **validated_data)