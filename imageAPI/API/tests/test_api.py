from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import reverse
from photo.models import Photo
from factories.input_factory import InputFactory


class TestAPI(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user("test", "test@test.com.pl", "test")
        self.client.login(username="test", password="test")
        InputFactory()

    def test_get_photos(self):
        response = self.client.get(reverse("photos-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["title"], "Example Title")

    def test_create_photo(self):
        response = self.client.post(
            "/api/photos/",
            {
                "album_id": 1,
                "title": "test",
                "URL": "https://via.placeholder.com/150/92",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Photo.objects.count(), 2)

    def test_update_image(self):
        change_value = "Changed title"
        response = self.client.patch(
            reverse("photos-detail", kwargs={"pk": Photo.objects.first().id}),
            {"title": change_value},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Photo.objects.first().title, change_value)

    def test_delete_photo(self):
        response = self.client.delete(
            reverse("photos-detail", kwargs={"pk": Photo.objects.first().id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Photo.objects.count(), 0)
