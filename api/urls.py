from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PerfumeViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('perfumes', PerfumeViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]