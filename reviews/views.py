from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    """
    API view to list reviews of a specific doctor and allow creating new reviews.
    Allows read for all and create only for authenticated users.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Returns reviews filtered by doctor_id from URL parameters.
        """
        doctor_id = self.kwargs.get("doctor_id")
        return Review.objects.filter(doctor_id=doctor_id)
    
    def perform_create(self, serializer):
        """
        Saves the review with the authenticated user as the author.
        """
        serializer.save(user=self.request.user)