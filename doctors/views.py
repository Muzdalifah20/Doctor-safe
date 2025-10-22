# from django.shortcuts import render
from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DepartmentSerializer, DoctorSerializer
from .models import Department, Doctor

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Department.
    Permissions: Read-only for anonymous, full for authorized users with model permissions.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class DoctorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Doctor.
    Supports filtering by specialization.
    Permissions: Read-only for anonymous, full for authorized users with model permissions.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['specialization']

