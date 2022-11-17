import requests
from API.serailizers.photo_import_serializer import PhotoImportSerializer
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ImportFromExternalAPIListView(APIView):
    """Internal API endpoint triggers import of data through external API"""

    URL: str = "https://jsonplaceholder.typicode.com/photos"
    response: Response = requests.get(URL)

    def get(self, request):

        if self.response.status_code == status.HTTP_200_OK:
            for record in self.response.json():
                serializer = PhotoImportSerializer(data=record)
                serializer.is_valid()
                serializer.save()

            return redirect("photos-list")

        else:
            return Response(self.response.status_code)
