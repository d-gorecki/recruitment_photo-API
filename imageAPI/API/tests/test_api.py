import os
import shutil

import factory
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import signals
from django.shortcuts import reverse
from django.test import override_settings
from photo.factories.input_factory import InputFactory
from photo.models import Photo
from rest_framework import status
from rest_framework.test import APITestCase

TEST_DIR = "test_data"


class TestAPI(APITestCase):
    @classmethod
    def setUpClass(cls):
        os.mkdir(os.path.join(settings.BASE_DIR, TEST_DIR))

    @factory.django.mute_signals(signals.post_save)
    def setUp(self) -> None:
        self.user = User.objects.create_user("test", "test@test.com.pl", "test")
        self.client.login(username="test", password="test")
        InputFactory()

    def test_get_photos(self):
        response = self.client.get(reverse("photos-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["title"], "Example Title")

    @override_settings(MEDIA_ROOT=TEST_DIR)
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

    @override_settings(MEDIA_ROOT=TEST_DIR)
    def test_update_photo(self):
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

    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass
