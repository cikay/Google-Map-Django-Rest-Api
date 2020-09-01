

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
            'id',
            'latitude',
            'longitude'
        )
       

class PolygonSerializer(serializers.ModelSerializer):
    coordinate = CoordinateSerializer(many=True)
    class Meta:
        model = Polygon
        fields = (
            'id',
            'coordinate'
        )

class RegionSerializer(serializers.ModelSerializer):
    polygon = PolygonSerializer(many=True)
    class Meta: 
        model = Region
        fields = (
            'id',
            'name',
            'polygon'
        )

class CitySerializer(serializers.ModelSerializer):
    polygon = PolygonSerializer(many=True)

    class Meta: 
        model = City
        fields = (
            'id',
            'name',
            'region',
            'polygon'
        )

class CountySerializer(serializers.ModelSerializer):
   
    class Meta: 
        model = County
        fields = (
            'id',
            'name',
            'polygon',
            'city'
        )

class DistrictSerializer(serializers.ModelSerializer):
  
    class Meta: 
        model = District
        fields = (
            'id',
            'name', 
            'county',
            'polygon'
        )

class NeighborhoodSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Neighborhood
        fields = (
            'id',
            'name',
            'polygon',
            'district'
        )
