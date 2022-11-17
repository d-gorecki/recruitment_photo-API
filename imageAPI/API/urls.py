from API.views.photos import PhotosViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"photos", viewset=PhotosViewSet, basename="photos")

urlpatterns = [
    path("", include(router.urls)),
]
