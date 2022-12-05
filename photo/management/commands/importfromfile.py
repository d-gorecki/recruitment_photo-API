import json
import os
from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand

from API.serailizers.photo_import_serializer import PhotoImportSerializer


class Command(BaseCommand):
    """Django command importing data from .json file through DRF serializer into database
    Import file location must be BASE_DIR/import_file/data.json"""

    FILE_PATH: str = os.path.join(settings.BASE_DIR, "import_file/data.json")

    def handle(self, *args, **options):
        with open(self.FILE_PATH) as f:
            data: Any = json.load(f)
        for record in data:
            serializer = PhotoImportSerializer(data=record)
            serializer.is_valid()
            serializer.save()
