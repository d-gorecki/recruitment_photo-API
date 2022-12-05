import requests
from API.serailizers.photo_import_serializer import PhotoImportSerializer
from django.core.management.base import BaseCommand
from rest_framework.response import Response


class Command(BaseCommand):
    """Django command importing data from external API file through DRF serializer into database"""

    URL: str = "https://jsonplaceholder.typicode.com/photos"
    response: Response = requests.get(URL).json()

    def handle(self, *args, **options):
        for record in self.response:
            serializer = PhotoImportSerializer(data=record)
            serializer.is_valid()
            serializer.save()
        self.stdout.write(self.style.SUCCESS("Successfully imported photos."))
