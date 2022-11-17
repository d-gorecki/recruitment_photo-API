import factory
from photo.models import Photo


class InputFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    album_id: int = 1
    title: str = "Example Title"
    width: int = 100
    height: int = 100
    dominant_color: str = "#000000"
    URL: str = "http://localhost:8000/photos/1.png"
    external_URL: str = "https://via.placeholder.com/150/92"
