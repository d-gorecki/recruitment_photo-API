from typing import Any

import requests
from django.conf import settings
from PIL import Image


class DominantColor:
    """DominantColor class containing static method get_dominant_color"""

    @staticmethod
    def get_dominant_color(pil_img: Image) -> str:
        """Return dominant color of the passed Image object in hex(str) format"""
        img: Image = pil_img.copy()
        img: Image = img.convert("RGB")
        img: Image = img.resize((1, 1), resample=0)
        dominant_color: tuple[str, ...] = img.getpixel((0, 0))
        return "#%02x%02x%02x" % dominant_color


class ImportPhoto:
    """ImportPhotos class containing static method download_photos_and_populate_db"""

    @staticmethod
    def download_photo(photo_id: int, external_url: str) -> str:
        """Download photo from passed URL"""
        external_url += ".png"
        img_path: str = f"{settings.MEDIA_ROOT}/{photo_id}.png"
        img: bytes = requests.get(external_url).content
        with open(img_path, "wb") as f:
            f.write(img)

        return img_path

    @staticmethod
    def calculate_record_data(img_path: str, photo_id: int) -> dict[str, Any]:
        """Calculate and return dict with Image parameters (dominant_color, width, height, local URL)"""
        record = dict()

        with Image.open(img_path) as im:
            record["dominant_color"]: str = DominantColor.get_dominant_color(im)
            record["width"]: int = im.width
            record["height"]: int = im.height
            record["URL"]: str = f"file://{img_path}"

        return record
