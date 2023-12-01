from rest_framework import serializers

from api.models import Locations, Items

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"
