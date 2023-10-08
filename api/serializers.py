from rest_framework import serializers
from .models import Perfume, Rating




class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = ('id', 'title', 'description')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'perfume')