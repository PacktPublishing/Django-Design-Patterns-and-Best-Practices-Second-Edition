from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.SightingDetails.as_view(),
         name='sighting_details'),
]
