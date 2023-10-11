from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PerfumeViewSet, RatingViewSet
from .views import RatingViewSet, UserViewSet

from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('perfumes', PerfumeViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]