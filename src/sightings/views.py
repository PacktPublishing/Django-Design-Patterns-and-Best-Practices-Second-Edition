from django.shortcuts import render
from django.views.generic import DetailView
from .models import Sighting


class SightingDetails(DetailView):
    model = Sighting
