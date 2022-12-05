from django.contrib import admin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "album_id",
        "title",
        "width",
        "height",
        "dominant_color",
        "URL",
    )
