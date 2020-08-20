

from rest_framework import serializers

from .models import (
    Coordinate,
    Region,
    City,
    Town,
    District,
    Neighborhood
)

class CoordinateSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    class Meta:
        model = Coordinate
       


class RegionSerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)
    # name = serializers.CharField(max_length=50)
    class Meta: 
        model = Region
        fields = (
            'name',
            
        )
       
class CitySerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)

    class Meta: 
        model = City
        fields = (
            'name', 
            'coordinates',
            'region'
        )

class TownSerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)

    class Meta: 
        model = Town
        fields = (
            'name', 
            'coordinates',
            'city'
        )

class DistrictSerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)

    class Meta: 
        model = District
        fields = (
            'name', 
            'coordinates',
            'town'
        )

class NeighborhoodSerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)

    class Meta: 
        model = Neighborhood
        fields = (
            'name', 
            'coordinates',
            'district'
        )