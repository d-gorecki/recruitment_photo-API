from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch
from django.conf import settings
import os
from photo.models import Photo


class TestCommands(TestCase):
    @patch(
        "photo.management.commands.importfromfile.Command.FILE_PATH",
        os.path.join(settings.BASE_DIR, "photo/tests/files/data.json"),
    )
    def test_importfromfile(self):
        call_command("importfromfile")
        self.assertEqual(Photo.objects.count(), 3)

    @patch(
        "photo.management.commands.importfromapi.Command.response",
        [
            {
                "albumId": 1,
                "id": 1,
                "title": "accusamus beatae ad facilis cum similique qui sunt",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952",
            }
        ],
    )
    def test_importfromapi(self):
        call_command("importfromapi")
        self.assertEqual(Photo.objects.count(), 1)
