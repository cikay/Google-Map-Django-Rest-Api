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
        region = Region.objects.get(pk=pk)
        coor_serializer = CoordinateSerializer(instance=region, data=request.data)
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
                polygon.save()
            else:
                print(form.errors)

        try:
            serializer.save().polygon.add(polygon.id)
           
        except Polygon.DoesNotExist:
            print('******************************')
        
        return Response(serializer.errors)
    
    
class CityDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        region = Region.objects.get(id=request.data['related_model_id'])
        try:
            city = City.objects.create(name=request.data.get('name'), region=region)
            city.polygon.add(polygon.id)
            print(f"city: {city}")
        except Exception as e:
            print(e)
        return Response()


class CountyDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        city = City.objects.get(id=request.data['related_model_id'])
        try:
            town = County.objects.create(name=request.data.get('name'), city=city)
            town.polygon.add(polygon.id)
            print(f"town: {town}")
        except Exception as e:
            print(e)
        return Response()

class DistrictDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        polygon.save()
        town = County.objects.get(id=request.data['related_model_id'])
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

