Django Custom User Authentication API
This Django app provides user authentication functionality with custom user model, token-based authentication, registration, login, logout, and profile management using Django REST Framework.

Features
Custom user model (CustomUser) extending Django's AbstractUser with profile picture support.

User registration with email, username, and password.

Token-based authentication (DRF Tokens).

User login with username and password to get auth token.

User logout by deleting auth token.

Retrieve, update, or delete authenticated user profile.

API views implemented with class-based views (APIView, generics).

Permissions handled for public and authenticated access.

No caching on profile view to ensure fresh data.

Models
CustomUser: Extends built-in user with an optional profile picture (profile_picture field).

Serializers
UserSerializer: Basic user fields (id, username).

UserRegistrationSerializer: For user signup; handles password and returns auth token.

UserLoginSerializer: For user login; validates credentials and returns token.

UserProfileSerializer: For profile viewing and updating, includes profile picture.

API Endpoints
POST /register/: Register new user.

POST /login/: Login and receive auth token.

POST /logout/: Logout user, requires token.

GET, PUT, DELETE /profile/: Manage authenticated user profile.

Usage
Add app to Django project.

Configure Django REST Framework and token authentication.

Run migrations to create user and token tables.

Use API endpoints for authentication flows.

Installation
bash
pip install django djangorestframework
Add 'rest_framework' and 'rest_framework.authtoken' to INSTALLED_APPS in settings.