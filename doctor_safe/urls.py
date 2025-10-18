 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("doctors.urls")),
    path('api/', include('reviews.urls')),
    path('api/', include('contacts.urls')),
]
