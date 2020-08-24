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
        polygon = Polygon.objects.none()
        for coordinate in coordinates:
            data = {
                'latitude'  : coordinate[1],
                'longitude' : coordinate[0],
            }
            form = CoordinateSerializer(data=data)
            
            print(f"form is valid: {form.is_valid()}")
            if form.is_valid():
                coor = form.save()
                polygon = Polygon.objects.create()
                polygon.coordinate.add(coor.id)
                polygon.save()
            else:
                print(form.errors)

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
        serializer = CitySerializer(data={'name' : request.data.get('name'), 'region': Region.objects.get(request.data['region_id'])})
        coordinates = request.data.get('polygon')
        print(f"city serializer is valid: {serializer.is_valid()}")
        polygon = Polygon.objects.none()
        print(f"coor: {coordinates}")
        for coordinate in coordinates:
            data = {
                'latitude'  : coordinate[1],
                'longitude' : coordinate[0],
            }
            form = CoordinateSerializer(data=data)
            
            print(f"form is valid: {form.is_valid()}")
            if form.is_valid():
                coor = form.save()
                polygon = Polygon.objects.create()
                polygon.coordinate.add(coor.id)
                polygon.save()
            else:
                print(form.errors)

        try:
            serializer.save().polygon.add(polygon.id)
            
            
        except Polygon.DoesNotExist:
            print('******************************')
        
        return Response(serializer.errors)