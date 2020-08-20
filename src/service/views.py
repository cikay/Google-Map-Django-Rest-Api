from django.shortcuts import render
import json
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from .models import (
    Coordinate,
    Region,
    City,
    Town,
    District,
    Neighborhood
)

from rest_framework.views import APIView
from .serializers import (
    CoordinateSerializer,
    RegionSerializer,
    CitySerializer,
    TownSerializer,
    DistrictSerializer,
    NeighborhoodSerializer
)

class RegionListCreateView(APIView):


    def post(self, request, *args, **kwargs):
        print(f"request: {request.data}")
        coor = CoordinateSerializer(latitude = request.data['coordinates'][1], longitude=request.data['coordinates'][0])
        serializer = RegionSerializer(coordinates = coor, name = request.data['name'])

        if serializer.is_valid():
            print('GELDI')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # def put(self, request, id):

    def get(self, request, *args, **kwargs):
        
        
        qs = Region.objects.all()
        serializer = RegionSerializer(qs, many= True)
        for i in serializer.data:
            print(i)
        return Response(serializer.data)


class CityListCreateView(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class TownListCreateView(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = TownSerializer
    queryset = Town.objects.all()

class DistrictListCreateView(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class NeighborhoodListCreateView(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    serializer_class = NeighborhoodSerializer
    queryset = Neighborhood.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



class Common:
    @classmethod
    def process(self, request):
        for latlong in request.data:
            list_latlong = json.loads(latlong)
            Coordinate.objects.create(latlong)


