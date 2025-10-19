from rest_framework import generics, permissions
from .models import ContactRequest
from .serializers import ContactRequestSerializer

class ContactRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactRequestSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        return ContactRequest.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
