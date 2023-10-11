from rest_framework import serializers
from rest_framework import serializers, status
from .models import Perfume, Rating

from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'perfume')