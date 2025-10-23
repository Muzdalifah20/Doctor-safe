from rest_framework import generics, permissions
from .models import ContactRequest
from .serializers import ContactRequestSerializer

class ContactRequestListCreateView(generics.ListCreateAPIView):
    """
    API view to list all contact requests (admin only) and allow authenticated users to create new requests.
    """
    serializer_class = ContactRequestSerializer

    def get_permissions(self):
        """
        Custom permission logic:
        - GET requests restricted to admin users.
        - POST requests allowed for authenticated users.
        """
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        """
        Returns all contact requests.
        """
        return ContactRequest.objects.all()

    def perform_create(self, serializer):
        """
        Saves the new contact request with the authenticated user as the creator.
        """
        serializer.save(user=self.request.user)
