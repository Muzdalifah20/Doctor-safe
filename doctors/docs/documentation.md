Doctor App Api Documentation

Overview:
The Doctors app provide restful apis to manage and access information regarding demical departments and doctors. The apis support CRUD operations and read-only permession for general users, while admins with editing privilages.

Models: 
1_Department
 fields:
    id(intiger, auto-generated)
    name(string)(e.g. Cardiology)

2_Doctor
 fields:
    id(intiger, auto-generated)
    Name(string) 
    specialization(foreign key to department)
    Pricing info(string)
    Safety_rating(Decimal)
    Verified (boolean, whether admin-verified)
    bio(text)
    contact info(string)

Endpoints

1_Department
    list departments:
    GET /api/departments/
    returns a list of all departments.

    Detail department:
    GET /api/deparments/<int:id>
    returns details of a single department.

    Create department(Admin only):
    POST /api/departments/

    Update department(Admin only):
    PUT /api/departments/<int:id>/

    Delete department(Admin only):
    DELETE /api/departments/<int:id>/


2_Doctors
    list doctors
    GET /api/doctors/
    returns a list all doctors

    detail doctor 
    GET /api/doctors/<int:id>/
    returns detail of a single doctor

    create doctor(Admin only):
    POST /api/doctors/

    Udate doctor(Admin only):
    PUT /api/doctors/<int:id>/

    delete doctor(Admin only):
    DELETE /api/doctors/<int:id>/

Permissions
    Read-only: all users can view lists and details.
    Write (create, update, delete): restricted to admin user with staff privilages.


