from PIL import Image
from django.conf import settings
import requests
from API.serailizers.photo_import_serializer import PhotoImportSerializer


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
    def download_photo(record: dict) -> str:
        if record.get("url"):
            url: str = record.get("url") + ".png"
        else:
            url: str = record.get("URL") + ".png"
        record_id: int = record.get("id")

        img_path: str = f"{settings.MEDIA_ROOT}/{record_id}.png"
        img: bytes = requests.get(url).content

        with open(img_path, "wb") as f:
            f.write(img)

        return img_path

    @staticmethod
    def calculate_record_data(record: dict, img_path: str) -> dict:
        record_id: int = record.get("id")

        with Image.open(img_path) as im:
            record["dominant_color"] = DominantColor.get_dominant_color(im)
            record["width"] = im.width
            record["height"] = im.height

        record["url"] = f"http://localhost:8000{settings.MEDIA_URL}{record_id}.png"

        if record.get("thumbnailUrl"):
            record.pop("thumbnailUrl")

        return record

    @staticmethod
    def save_to_db(record: dict):
        serializer: PhotoImportSerializer = PhotoImportSerializer(data=record)
        serializer.is_valid()
        serializer.save()
