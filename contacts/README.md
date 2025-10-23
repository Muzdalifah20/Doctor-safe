Contact Requests API
This Django app allows users to send contact requests to doctors and enables administrators to view all requests.

Features
ContactRequest model with fields for user, doctor name, request details, status, and timestamp.

Status field supports 'pending', 'approved', and 'rejected' states.

Serializer enforces read-only user and status fields.

API view to list all requests (admin only) and create requests (authenticated users).

Permissions ensure only admins can list requests, while authenticated users can submit new ones.

Models
ContactRequest: Represents a user’s request to contact a specific doctor, with approval status.

API Endpoints
GET /contact-requests/: List all contact requests (admin only).

POST /contact-requests/: Create a new contact request (authenticated users).

Permissions
GET access restricted to admins.

POST access allowed for authenticated users.

Usage
Add the contact request app to your Django project.

Configure URLs to point to ContactRequestListCreateView.

Set up authentication for users and admin.

Use API to manage contact requests respecting permissions.

Installation
bash
pip install django djangorestframework
Add 'rest_framework' and the contact requests app to INSTALLED_APPS in settings.py.