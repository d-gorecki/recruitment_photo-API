from django.urls import path, include
from rest_framework.routers import DefaultRouter

from API.views.import_from_API import ImportFromExternalAPIListView
from API.views.import_from_file import ImportFromFileView
from API.views.photos import PhotosViewSet

router = DefaultRouter()
router.register(r"photos", viewset=PhotosViewSet, basename="photos")

urlpatterns = [
    path("import_from_API/", ImportFromExternalAPIListView.as_view()),
    path("import_from_file/", ImportFromFileView.as_view()),
    path("", include(router.urls)),
]
