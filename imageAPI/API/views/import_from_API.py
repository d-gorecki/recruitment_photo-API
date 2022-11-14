from rest_framework.views import APIView
from rest_framework.response import Response
from photo.functionality import ImportPhoto
from photo.models import Photo
from API.serailizers.photo_serializer import PhotoSerializer
import requests
from django_q.tasks import async_task


class ImportFromExternalAPIListView(APIView):
    """Internal API endpoint triggers import of data through external API"""

    def get(self, request):
        URL = "https://jsonplaceholder.typicode.com/photos"
        response = requests.get(URL)

        if response.status_code == 200:
            ImportPhoto.download_photos_and_populate_db(response.json()[:3])
            photos = Photo.objects.all()
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)

        else:
            return Response(response.status_code)
