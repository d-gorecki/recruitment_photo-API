from django.db import models


class Photo(models.Model):
    album_id = models.IntegerField()
    title = models.CharField(max_length=240, help_text="photo title")
    width = models.IntegerField(help_text="photo width", null=True)
    height = models.IntegerField(help_text="photo height", null=True)
    dominant_color = models.CharField(
        max_length=7, help_text="photo dominant color in hex format", null=True
    )
    URL = models.ImageField(upload_to="", null=True)
