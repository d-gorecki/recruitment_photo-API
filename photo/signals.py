from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from photo.functionality import ImportPhoto
from photo.models import Photo


@receiver(post_save, sender=Photo)
def update_photo(sender, instance, created, **kwargs):
    img_path: str = ImportPhoto.download_photo(instance.id, instance.external_URL)
    calculated_data: dict[str, Any] = ImportPhoto.calculate_record_data(
        img_path, instance.id
    )
    Photo.objects.filter(id=instance.id).update(
        width=calculated_data.get("width"),
        height=calculated_data.get("height"),
        dominant_color=calculated_data.get("dominant_color"),
        URL=calculated_data.get("URL"),
    )
