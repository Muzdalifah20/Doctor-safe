from django.urls import path
from .views import ReviewListCreateView

urlpatterns = [
    path('doctors/<int:doctor_id>/reviews/', ReviewListCreateView.as_view(), name='doctor-reviews'),
]