import requests
from django.core.management.base import BaseCommand
from photo.functionality import ImportPhoto
from rest_framework.response import Response


class Command(BaseCommand):
    """Django command importing data from external API file through DRF serializer into database"""

    URL: str = "https://jsonplaceholder.typicode.com/photos"
    response: Response = requests.get(URL).json()

    def handle(self, *args, **options):
        for record in self.response:
            img_path: str = ImportPhoto.download_photo(record)
            ImportPhoto.save_to_db(ImportPhoto.calculate_record_data(record, img_path))
