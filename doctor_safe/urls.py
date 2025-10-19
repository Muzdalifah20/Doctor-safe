 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("", include("accounts.urls")),
    path("", include("doctors.urls"))
=======
    path("", include("accounts.urls"))
>>>>>>> 7770ddfcabb1df31a75bc7add3e6c8f113cd882d
]
