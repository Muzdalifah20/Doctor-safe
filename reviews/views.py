from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")
        return Review.objects.filter(doctor_id=doctor_id)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)