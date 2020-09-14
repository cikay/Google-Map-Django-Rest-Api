

from rest_framework import serializers

from .models import (
    Coordinate,
    Region,
    City,
    County,
    # District,
    Neighborhood
)

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = (
            'id',
            'lat',
            'lng',
        )
       
class RegionSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    model = serializers.SerializerMethodField()
    class Meta: 
        model = Region
        fields = (
            'id',
            'model',
            'name',
            'coordinates',
        )
    
    def get_model(self, instance):
        try:
            return instance.__class__.__name__
        except:
            return None

class CitySerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    model = serializers.SerializerMethodField()
    class Meta: 
        model = City
        fields = (
            'id',
            'model',
            'name',
            'region',
            'coordinates',
        )

    def get_model(self, instance):
        try:
            return instance.__class__.__name__
        except:
            return None


class CountySerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    model = serializers.SerializerMethodField()
    class Meta: 
        model = County
        fields = (
            'id',
            'model',
            'name',
            'coordinates',
            'city',
        )

    def get_model(self, instance):
        try:
            return instance.__class__.__name__
        except:
            return None


class NeighborhoodSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)
    model = serializers.SerializerMethodField()
    class Meta: 
        model = Neighborhood
        fields = (
            'id',
            'model',
            'name',
            'coordinates',
            'county',
        )

    def get_model(self, instance):
        try:
            return instance.__class__.__name__
        except:
            return None