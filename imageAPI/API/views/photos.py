import json
import os
from typing import Any

import requests
from API.serailizers.photo_create_update_serializer import \
    PhotoCreateUpdateSerializer
from API.serailizers.photo_import_serializer import PhotoImportSerializer
from API.serailizers.photo_serializer import PhotoSerializer
from django.conf import settings
from django.db.models import QuerySet
from django.shortcuts import redirect
from photo.models import Photo
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class PhotosViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Photo] = Photo.objects.all()
    permission_classes: list[permissions] = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class: PhotoSerializer = PhotoSerializer
    serializer_action_classes: dict[str, serializers.ModelSerializer] = {
        "create": PhotoCreateUpdateSerializer,
        "update": PhotoCreateUpdateSerializer,
        "list": PhotoSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(
            self.action, super().get_serializer_class()
        )

    @action(detail=False)
    def import_from_api(self, request):
        """Internal API endpoint triggers import of data through external API"""

        URL: str = "https://jsonplaceholder.typicode.com/photos"
        response: Response = requests.get(URL)

        if response.status_code == status.HTTP_200_OK:
            for record in response.json():
                serializer = PhotoImportSerializer(data=record)
                serializer.is_valid()
                serializer.save()

            return redirect("photos-list")

        else:
            return Response(response.status_code)

    @action(detail=False)
    def import_from_file(self, request):
        """Internal API endpoint triggers import of data through .json file
        Import file location must be BASE_DIR/import_file/data.json"""

        FILE_PATH: str = os.path.join(settings.BASE_DIR, "import_file/data.json")

        try:
            with open(FILE_PATH, "r") as f:
                data: Any = json.load(f)
            for record in data:
                serializer = PhotoImportSerializer(data=record)
                serializer.is_valid()
                serializer.save()

            return redirect("photos-list")

        except (FileNotFoundError, IOError):
            return Response({"error": "file does not exist"})
