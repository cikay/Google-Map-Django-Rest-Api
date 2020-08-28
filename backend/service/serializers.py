

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

    class Meta: 
        model = Region
        fields = (
            'id',
            'name',
            'polygon'
        )
       
class CitySerializer(serializers.ModelSerializer):
   
    class Meta: 
        model = City
        fields = (
            'name', 
            'region',
            'polygon'
        )

class CountySerializer(serializers.ModelSerializer):
   
    class Meta: 
        model = County
        fields = (
            'name', 
            'coordinates',
            'city'
        )

class DistrictSerializer(serializers.ModelSerializer):
  
    class Meta: 
        model = District
        fields = (
            'name', 
            'coordinates',
            'county'
        )

class NeighborhoodSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Neighborhood
        fields = (
            'name', 
            'coordinates',
            'district'
        )