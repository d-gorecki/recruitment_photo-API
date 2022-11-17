import os
from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from photo.functionality import DominantColor, ImportPhoto
from PIL import Image


class TestFunctionality(TestCase):
    def setUp(self) -> None:
        self.img_path = os.path.join(
            settings.BASE_DIR, "photo/tests/files/black_100x100.png"
        )
        self.data = {
            "dominant_color": "#000000",
            "width": 100,
            "height": 100,
            "URL": "http://localhost:8000/photos/1.png",
        }

    def test_get_dominant_color(self):
        with Image.open(self.img_path) as im:
            hex = DominantColor.get_dominant_color(im)
        self.assertEqual(hex, "#000000")

    @patch(
        "photo.functionality.DominantColor.get_dominant_color", return_value="#000000"
    )
    def test_calculate_record_data(self, get_dominant_color):
        actual = ImportPhoto.calculate_record_data(self.img_path, 1)
        self.assertEqual(self.data, actual)
