from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.ShowProfile.as_view(), name='show_me'),
    path('<slug:slug>/', views.ShowProfile.as_view(),
         name='show_user'),
]
