import requests
from django.core.management.base import BaseCommand
from photo.functionality import ImportPhoto


class Command(BaseCommand):
    """Django command importing data from external API file through DRF serializer into database"""

    URL = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(URL).json()

    def handle(self, *args, **options):
        for record in self.response:
            img_path = ImportPhoto.download_photo(record)
            ImportPhoto.save_to_db(ImportPhoto.calculate_record_data(record, img_path))
