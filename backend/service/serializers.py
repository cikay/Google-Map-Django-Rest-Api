

from rest_framework import serializers

from .models import (
    Coordinate,
    Polygon,
    Region,
    City,
    County,
    District,
    Neighborhood
)

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = (
            'latitude',
            'longitude'
        )
       

class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = (
            'coordinate'
        )

class RegionSerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)
    # name = serializers.CharField(max_length=50)
    class Meta: 
        model = Region
        fields = (
            'id',
            'name',
            'polygon'
        )
       
class CitySerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)
    # polygon = PolygonSerializer(many=True)
    
    class Meta: 
        model = City
        fields = (
            'name', 
            'region',
            'polygon'
        )

class CountySerializer(serializers.ModelSerializer):
    # coordinates = CoordinateSerializer(many=True)

    class Meta: 
        model = County
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
            'county'
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