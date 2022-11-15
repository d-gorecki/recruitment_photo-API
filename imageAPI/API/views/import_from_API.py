import requests
from API.serailizers.photo_serializer import PhotoSerializer
from django.db.models import QuerySet
from photo.functionality import ImportPhoto
from photo.models import Photo
from rest_framework.response import Response
from rest_framework.views import APIView


class ImportFromExternalAPIListView(APIView):
    """Internal API endpoint triggers import of data through external API"""

    URL: str = "https://jsonplaceholder.typicode.com/photos"
    response: Response = requests.get(URL)

    def get(self, request):

        if self.response.status_code == 200:
            for record in self.response.json():
                img_path: str = ImportPhoto.download_photo(record)
                ImportPhoto.save_to_db(
                    ImportPhoto.calculate_record_data(record, img_path)
                )
            photos: QuerySet[Photo] = Photo.objects.all()
            serializer: PhotoSerializer = PhotoSerializer(photos, many=True)
            return Response(serializer.data)

        else:
            return Response(self.response.status_code)
