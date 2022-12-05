import os
import shutil
from unittest.mock import patch

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase, override_settings

from photo.models import Photo

TEST_DIR = "test_data"


class TestCommands(TestCase):
    @classmethod
    def setUpClass(cls):
        os.mkdir(os.path.join(settings.BASE_DIR, TEST_DIR))

    @patch(
        "photo.management.commands.importfromfile.Command.FILE_PATH",
        os.path.join(settings.BASE_DIR, "photo/tests/files/data.json"),
    )
    @override_settings(MEDIA_ROOT=TEST_DIR)
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
    @override_settings(MEDIA_ROOT=TEST_DIR)
    def test_importfromapi(self):
        call_command("importfromapi")
        self.assertEqual(Photo.objects.count(), 1)

    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass
