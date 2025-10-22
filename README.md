Authentication API
Register
URL: /register/

Method: POST

Payload:

json
{
  "email": "user@example.com",
  "username": "user123",
  "password": "password123"
}
Response:

User profile info with auth token

Login
URL: /login/

Method: POST

Payload:

json
{
  "username": "user123",
  "password": "password123"
}
Response:

Auth token for session management

Usage
Use the token provided in Authorization: Token <token> header for authenticated requests.

Departments API
Add Department
URL: /departments/

Method: POST

Payload:

json
{
  "name": "Cardiology"
}
Note: Requires appropriate permissions.

List Departments
URL: /departments/

Method: GET

Doctors API
Add Doctor
URL: /doctors/

Method: POST

Payload:

json
{
  "name": "Dr. Smith",
  "specialization_id": 1,
  "pricing_info": "Consultation: $100",
  "safety_rating": 4.8,
  "verified": true,
  "bio": "Experienced cardiologist",
  "contact_info": "email@example.com",
  "image": "<image file via multipart form>"
}
Note: Requires appropriate permissions.

List and Filter Doctors
URL: /doctors/?specialization=1

Method: GET

Reviews API
Add Review
URL: /doctors/<doctor_id>/reviews/

Method: POST

Payload:

json
{
  "rating": 5,
  "comment": "Excellent care and attention!"
}
Note: User associated with review from auth token.

List Reviews
URL: /doctors/<doctor_id>/reviews/

Method: GET

Contact Requests API
Submit Contact Request
URL: /contact-requests/

Method: POST

Payload:

json
{
  "doctor_name": "Dr. Smith",
  "request_details": "I would like to schedule an appointment."
}
Note: Authenticated user is automatically assigned.

List Contact Requests (Admin only)
URL: /contact-requests/

Method: GET