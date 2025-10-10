# from django.shortcuts import render
from rest_framework import viewsets,permissions
 
from .serializers import DepartmentSerializer, DoctorSerializer
from .models import Department, Doctor

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

