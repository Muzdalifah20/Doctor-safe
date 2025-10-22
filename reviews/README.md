Doctor Reviews API
This Django app provides RESTful API endpoints to allow users to review doctors by submitting ratings and comments.

Features
Review model linking users and doctors with rating (1 to 5) and text comment.

Automatically stores timestamp of each review.

Serializer to validate and serialize review data.

API view to list reviews of a doctor, and create new reviews.

Permissions allow anyone to read reviews, but only authenticated users can submit reviews.

Models
Review: Links user and doctor with a rating (validated between 1 and 5), comment text, and timestamp.

API Endpoints
GET /doctors/<doctor_id>/reviews/: List all reviews for a specific doctor.

POST /doctors/<doctor_id>/reviews/: Submit a new review for a specific doctor (authentication required).

Permissions
Read access for all users.

Write access restricted to authenticated users.

Usage
Include the reviews app in the Django project.

Add URL routing for the ReviewListCreateView with doctor_id parameter.

Ensure REST framework authentication is set up for user login.

Use API to display and gather doctor reviews.

Installation
bash
pip install django djangorestframework
Add 'rest_framework' and the reviews app to INSTALLED_APPS in settings.py.