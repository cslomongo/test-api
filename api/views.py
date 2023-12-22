from django.shortcuts import render

from rest_framework import generics, permissions, authentication 

from .models import Items,Locations
from api.permissions import isStaffEditor
from api.serializers import LocationSerializer, ItemSerializer

# Create your views here.

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [isStaffEditor]
    authentication_classes = [authentication.SessionAuthentication]

    def get_queryset(self):
        queryset = Items.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset

class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Locations.objects.all()
    permission_classes = [isStaffEditor]
    authentication_classes = [authentication.SessionAuthentication]


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Locations.objects.all()
    permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    