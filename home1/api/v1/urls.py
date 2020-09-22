from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import USViewSet

router = DefaultRouter()
router.register("us", USViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
