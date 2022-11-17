import json
import os
from typing import Any

from API.serailizers.photo_import_serializer import PhotoImportSerializer
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView


class ImportFromFileView(APIView):
    """Internal API endpoint triggers import of data through .json file
    Import file location must be BASE_DIR/import_file/data.json"""

    FILE_PATH: str = os.path.join(settings.BASE_DIR, "import_file/data.json")

    def get(self, request):

        try:
            with open(self.FILE_PATH, "r") as f:
                data: Any = json.load(f)
            for record in data:
                serializer = PhotoImportSerializer(data=record)
                serializer.is_valid()
                serializer.save()

            return redirect("photos-list")

        except (FileNotFoundError, IOError):
            return Response({"error": "file does not exist"})
