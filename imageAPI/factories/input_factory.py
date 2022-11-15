import factory
from photo.models import Photo


class InputFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    album_id = 1
    title = "Example Title"
    width = 100
    height = 100
    dominant_color = "#000000"
    URL = "http://localhost:8000/photos/1.png"
