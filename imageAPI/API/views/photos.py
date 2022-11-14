from rest_framework import viewsets
from photo.models import Photo
from API.serailizers.photo_serializer import PhotoSerializer
from rest_framework import permissions


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
