from django.shortcuts import render
from django.http import JsonResponse
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
    County,
    District,
    Neighborhood
)

from rest_framework.views import APIView
from .serializers import (
    CoordinateSerializer,
    PolygonSerializer,
    RegionSerializer,
    CitySerializer,
    CountySerializer,
    DistrictSerializer,
    NeighborhoodSerializer
)



class RegionList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (permissions.AllowAny, )


class RegionDetail(APIView):
 
    def put(self, request, pk):
        print(request.data)
        region = Region.objects.get(pk=pk)
        coor_serializer = CoordinateSerializer(instance=region, data=request.data)
        
        if coor_serializer.is_valid():
            coor_serializer.save()
            return Response(coor_serializer.data)
        return Response(coor_serializer.errors)
    
    def post(self, request):
        print('posting')
        polygon = create_polygon(request)
        print('posting devam ediyor')
        try:
            region = Region.objects.create(name=request.data.get('name'), polygon=polygon)
            print('region kaydedildi')
        except Polygon.DoesNotExist:
            print('******************************')
        
        return Response()
        
    

class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.AllowAny, )

class CityDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        region = Region.objects.get(id=request.data['related_model_id'])
        try:
            city = City.objects.create(name=request.data.get('name'), region=region)
            city.polygon.add(polygon.id)
            print(f"city: {city}")
        except Exception as e:
            print(e)
        return Response()

class CountyList(ListAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = (permissions.AllowAny, )

class CountyDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        city = City.objects.get(id=request.data['related_model_id'])
        try:
            county = County.objects.create(name=request.data.get('name'), city=city)
            county.polygon.add(polygon.id)
            print(f"county: {county}")
        except Exception as e:
            print(e)
        return Response()

class DistrictList(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (permissions.AllowAny, )

class DistrictDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        town = County.objects.get(id=request.data['related_model_id'])
        try:
            district = District.objects.create(name=request.data.get('name'), town=town)
            town.polygon.add(polygon.id)
            print(f"district: {district}")
        except Exception as e:
            print(e)
        return Response()

class NeighborhoodList(ListAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = (permissions.AllowAny, )

class NeighborhoodDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        district = District.objects.get(id=request.data['related_model_id'])
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
    polygon.save()
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
    print(polygon)
    return polygon

