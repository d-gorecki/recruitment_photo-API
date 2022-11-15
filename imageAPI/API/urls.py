from API.views.import_from_API import ImportFromExternalAPIListView
from API.views.import_from_file import ImportFromFileView
from API.views.photos import PhotosViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"photos", viewset=PhotosViewSet, basename="photos")

urlpatterns = [
    path(
        "import_from_API/", ImportFromExternalAPIListView.as_view(), name="import-api"
    ),
    path("import_from_file/", ImportFromFileView.as_view(), name="import-file"),
    path("", include(router.urls)),
]
