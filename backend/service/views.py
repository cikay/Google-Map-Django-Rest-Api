from django.shortcuts import render
import json
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
)

from rest_framework import permissions
from rest_framework import mixins
from rest_framework.response import Response

from .models import (
    Coordinate,
    Polygon,
    Region,
    City,
    Town,
    District,
    Neighborhood
)

from rest_framework.views import APIView
from .serializers import (
    CoordinateSerializer,
    PolygonSerializer,
    RegionSerializer,
    CitySerializer,
    TownSerializer,
    DistrictSerializer,
    NeighborhoodSerializer
)

class NeighborhoodDetail(APIView):

    def post(self, request):
        serializer = NeighborhoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class RegionList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (permissions.AllowAny, )


class RegionDetail(APIView):
 
    def put(self, request, pk):
        print(request.data)
        print(f"pk: {pk}")
        region = Region.objects.get(pk=pk)
        print(f"region instance: {Region.objects.get(pk=pk)}")
        coor_serializer = CoordinateSerializer(instance=region, data=request.data)
        print(f"coor_serializer: {coor_serializer}")
        print(f"coor_serializer.is_valid() {coor_serializer.is_valid()}")
        if coor_serializer.is_valid():
            coor_serializer.save()
            return Response(coor_serializer.data)
        return Response(coor_serializer.errors)
    
    def post(self, request):
        serializer = RegionSerializer(data={'name' : request.data.get('name')})
        print(serializer)
        coordinates = request.data.get('polygon')
        # request.data['polygon'])
        # region = Region()
        print(f"serializer is valid: {serializer.is_valid()}")
        polygon = Polygon.objects.create()
        for coordinate in coordinates:
            data = {
                'latitude'  : coordinate[1],
                'longitude' : coordinate[0],
            }
            form = CoordinateSerializer(data=data)
            
            print(f"form is valid: {form.is_valid()}")
            if form.is_valid():
                coor = form.save()
                
                polygon.coordinate.add(coor.id)
                
            else:
                print(form.errors)

        polygon.save()

        try:
            serializer.save().polygon.add(polygon.id)
           
        except Polygon.DoesNotExist:
            print('******************************')
        
        # if serializer.is_valid():
        #     # region = serializer.save()
        #     # print(f"region: {region}")


        return Response(serializer.errors)

    
class CityDetail(APIView):


    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        region = Region.objects.get(id=request.data['region_id'])
        print(f"city id: {request.data['city_id']}")
        try:
            city = City.objects.create(name=request.data.get('name'), region=region)
            city.polygon.add(polygon.id)
            print(f"city: {city}")
        except Exception as e:
            print(e)
        return Response()


class TownDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        city = City.objects.get(id=request.data['city_id'])
        try:
            town = Town.objects.create(name=request.data.get('name'), city=city)
            town.polygon.add(polygon.id)
            print(f"town: {town}")
        except Exception as e:
            print(e)
        return Response()

class DistrictDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        town = Town.objects.get(id=request.data['town_id'])
        try:
            district = District.objects.create(name=request.data.get('name'), town=town)
            town.polygon.add(polygon.id)
            print(f"district: {district}")
        except Exception as e:
            print(e)
        return Response()

class NeighborhoodDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        district = District.objects.get(id=request.data['district_id'])
        try:
            neighborhood = Neighborhood.objects.create(name=request.data.get('name'), district=district)
            neighborhood.polygon.add(polygon.id)
            print(f"neighborhood: {neighborhood}")
        except Exception as e:
            print(e)
        return Response()

def create_polygon(request) ->  Polygon: 

    coordinates = request.data.get('polygon')
    polygon = Polygon.objects.create()
    for coordinate in coordinates:
        data = {
            'latitude'  : coordinate[1],
            'longitude' : coordinate[0],
        }
        form = CoordinateSerializer(data=data)
        
        if form.is_valid():
            coor = form.save()
            polygon.coordinate.add(coor.id)
        else:
            print(form.errors)
    return polygon

