import requests
from django.core.management.base import BaseCommand
from django.conf import settings
import os
from photo.functionality import ImportPhoto


class Command(BaseCommand):
    """Django command importing data from external API file through DRF serializer into database"""

    FILE_PATH = os.path.join(settings.BASE_DIR, "import_file/data.json")
    URL = "https://jsonplaceholder.typicode.com/photos"

    def handle(self, *args, **options):
        response = requests.get(self.URL).json()
        ImportPhoto.download_photos_and_populate_db(response)
