Doctors and Departments Management API
This Django app provides backend API for managing medical departments and doctors with detailed information such as specialization, pricing, safety rating, and contact info.

Features
Department model representing medical specialties.

Doctor model with fields for name, specialization, pricing, safety rating, verification status, bio, contact, and image.

DRF serializers for input validation and JSON representation.

RESTful API endpoints for CRUD operations via ModelViewSet.

Filtering support to filter doctors by specialization.

Permission handling allowing read-only access to anonymous users and full access to authorized users with appropriate model permissions.

Admin registration for easy management in Django admin interface.

Models
Department: Holds medical department name.

Doctor: Represents doctors linked to departments, including profile and professional details.

API Endpoints
/departments/: List, create, update, delete departments.

/doctors/: List, create, update, delete doctors with ability to filter doctors by specialization.

Permissions
Anonymous users have read-only access.

Authenticated users with appropriate model permissions can create, update, or delete records.

Usage
Add the doctors app to your Django project.

Configure Django REST Framework and Django Filters.

Include app URLs wired to the viewsets for RESTful endpoints.

Run migrations to create models in the database.

Use the API with proper authentication and permissions for management.

Installation
bash
pip install django djangorestframework django-filter
Add 'rest_framework', 'django_filters', and the doctors app to INSTALLED_APPS in settings.py.