from django.urls import path
from API.views.import_from_API import ImportFromExternalAPIListView
from API.views.import_from_file import ImportFromFileView

urlpatterns = [
    path("import_from_API/", ImportFromExternalAPIListView.as_view()),
    path("import_from_file/", ImportFromFileView.as_view()),
]
