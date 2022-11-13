from django.core.management.base import BaseCommand
import json
from django.conf import settings
import os
from photo.functionality import ImportPhoto


class Command(BaseCommand):
    """"""

    FILE_PATH = os.path.join(settings.BASE_DIR, "import_file/data.json")

    def handle(self, *args, **options):
        with open(self.FILE_PATH) as f:
            data = json.load(f)

            ImportPhoto.download_photos_and_populate_db(data)
