from django.db import models


class Photo(models.Model):
    album_id = models.IntegerField(help_text="Album ID")
    title = models.CharField(max_length=240, help_text="Photo title")
    width = models.IntegerField(help_text="Photo width", null=True)
    height = models.IntegerField(help_text="Photo height", null=True)
    dominant_color = models.CharField(
        max_length=7, help_text="Photo dominant color in hex format", null=True
    )
    URL = models.ImageField(
        upload_to="", null=True, help_text="URL to locally stored file"
    )
    external_URL = models.URLField(null=True, help_text="external URL")
