import json
import os
from typing import Any

from API.serailizers.photo_serializer import PhotoSerializer
from django.conf import settings
from django.db.models import QuerySet
from photo.functionality import ImportPhoto
from photo.models import Photo
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
                img_path: str = ImportPhoto.download_photo(record)
                ImportPhoto.save_to_db(
                    ImportPhoto.calculate_record_data(record, img_path)
                )
            photos: QuerySet[Photo] = Photo.objects.all()
            serializer: PhotoSerializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)

        except (FileNotFoundError, IOError):
            return Response({"error": "file does not exist"})
