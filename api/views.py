from django.shortcuts import render

# Create your views here.
from rest_framework import request, status,  viewsets
from .models import Perfume, Rating
from .serializers import PerfumeSerializer, RatingSerializer
from rest_framework.decorators import action

from rest_framework.response import Response

from django.contrib.auth.models import User

class PerfumeViewSet(viewsets.ModelViewSet):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer

    @action(detail=True, methods=['post'])
    def rate_Perfume(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update 
            '''
            Perfume = Perfume.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Perfume Rate Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_400_BAD_REQUEST)

            except:
                # create if the rate not exist 
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                json = {
                    'message': 'Perfume Rate Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer