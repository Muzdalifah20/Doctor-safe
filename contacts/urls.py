from django.urls import path
from .views import ContactRequestListCreateView

urlpatterns = [
    path('contacts/', ContactRequestListCreateView.as_view(), name='contact-requests'),
]
