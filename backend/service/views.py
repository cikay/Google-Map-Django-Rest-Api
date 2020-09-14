from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import Http404
from rest_framework import status
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
    Region,
    City,
    County,
    # District,
    Neighborhood
)

from rest_framework.views import APIView
from .serializers import (
    CoordinateSerializer,
    # PolygonSerializer,
    RegionSerializer,
    CitySerializer,
    CountySerializer,
    # DistrictSerializer,
    NeighborhoodSerializer
)



class RegionList(ListAPIView):
    print('regions getting')
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
        name = request.data.get('name')
        exist = Region.objects.filter(name=name).exists()
        print(f"exist: {exist}")
        if exist: return Response()
        try: 

            region = Region.objects.create(name=request.data.get('name'))
            coordinates = request.data.get('polygon')
            for coordinate in coordinates:
                data = {
                    'lat'  : coordinate[1],
                    'lng' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    region.coordinates.add(coor.id)
                else:
                    print(form.errors)
            print("region kaydedildi")
        except Exception as e:
            print(e)
        return Response()
    
    def get(self, request):
        region = Region.objects.filter(id=2)
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        print('region deleting')
        region = self.get_object(pk=pk)
        print(region.coordinates)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try: 
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404


class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.AllowAny, )

class CityDetail(APIView):

    def post(self, request):
        name = request.data.get('name')
        exist = City.objects.filter(name=name).exists()
        print(f"exist: {exist}")
        if exist: return Response()
        region = Region.objects.get(name=request.data['related_model_name'])
        try:
            city = City.objects.create(name=name, region=region)
            coordinates = request.data.get('polygon')
            for coordinate in coordinates:
                data = {
                    'lat'  : coordinate[1],
                    'lng' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    city.coordinates.add(coor.id)
                else:
                    print(form.errors)
            print("city kaydedildi")
        except Exception as e:
            print(e)
        return Response()
    

    def get(self, request, *args, **kwargs):
        print('cities getting')
        related_model_id = kwargs['related_model_id']
        cities = City.objects.filter(region_id=related_model_id)
        serializer = CitySerializer(cities, many=True)
        # print(serializer)
        # print(serializer)
        return Response(serializer.data)
        

class CountyList(ListAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = (permissions.AllowAny, )

class CountyDetail(APIView):

    def post(self, request):
        name = request.data.get('name')
        exist = County.objects.filter(name=name).exists()
        print(f"exist: {exist}")
        if exist: return Response()
        city = City.objects.get(name=request.data['related_model_name'])
        try:
            county = County.objects.create(name=name, city=city)
            coordinates = request.data.get('polygon')
            for coordinate in coordinates:
                data = {
                    'lat'  : coordinate[1],
                    'lng' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    county.coordinates.add(coor.id)
                else:
                    print(form.errors)
        except Exception as e:
            print(e)
        return Response()

    def get(self, request, *args, **kwargs):
        related_model_id = kwargs['related_model_id']
        counties = County.objects.filter(city_id=related_model_id)
        serializer = CountySerializer(counties, many=True)
        return Response(serializer.data)



class NeighborhoodList(ListAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = (permissions.AllowAny, )

class NeighborhoodDetail(APIView):

    def post(self, request):
        county = County.objects.get(name=request.data['related_model_name'])
        try:
            neighborhood = Neighborhood.objects.create(name=request.data.get('name'), county=county)
            coordinates = request.data.get('polygon')
            for coordinate in coordinates:
                data = {
                    'lat'  : coordinate[1],
                    'lng' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    neighborhood.coordinates.add(coor.id)
                else:
                    print(form.errors)
        except Exception as e:
            print(e)
        return Response()
    
    def get(self, request, *args, **kwargs):
        related_model_id = kwargs['related_model_id']
        neighborhoods = Neighborhood.objects.filter(county_id=related_model_id)
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        return Response(serializer.data)



