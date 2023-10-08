from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Perfume, Rating
from .serializers import PerfumeSerializer, RatingSerializer


class PerfumeViewSet(viewsets.ModelViewSet):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer