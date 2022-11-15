from rest_framework.views import APIView
from rest_framework.response import Response
from photo.functionality import ImportPhoto
from photo.models import Photo
from API.serailizers.photo_serializer import PhotoSerializer
import requests
from django_q.tasks import async_task


class ImportFromExternalAPIListView(APIView):
    """Internal API endpoint triggers import of data through external API"""

    URL = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(URL)

    def get(self, request):

        if self.response.status_code == 200:
            for record in self.response.json():
                img_path = ImportPhoto.download_photo(record)
                ImportPhoto.save_to_db(
                    ImportPhoto.calculate_record_data(record, img_path)
                )
            photos = Photo.objects.all()
            serializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)

        else:
            return Response(self.response.status_code)
