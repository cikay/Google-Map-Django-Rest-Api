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
                polygon = Polygon.objects.create()
                data = {
                    'latitude'  : coordinate[1],
                    'longitude' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    polygon.coordinate.add(coor.id)
                    region.polygon.add(polygon.id)
                else:
                    print(form.errors)
            print("region kaydedildi")
        except Polygon.DoesNotExist:
            print('hata olustu, region kaydedilemedi')
        return Response()
    
   

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
                polygon = Polygon.objects.create()
                data = {
                    'latitude'  : coordinate[1],
                    'longitude' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    polygon.coordinate.add(coor.id)
                    city.polygon.add(polygon.id)
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
                polygon = Polygon.objects.create()
                data = {
                    'latitude'  : coordinate[1],
                    'longitude' : coordinate[0],
                }
                form = CoordinateSerializer(data=data)
                if form.is_valid():
                    coor = form.save()
                    polygon.coordinate.add(coor.id)
                    county.polygon.add(polygon.id)
                else:
                    print(form.errors)
        except Exception as e:
            print(e)
        return Response()

    def get(self, request, *args, **kwargs):
        related_model_id = kwargs['related_model_id']
        counties = County.objects.filter(city_id=related_model_id)
        print(counties)
        serializer = CountySerializer(counties, many=True)
        print(serializer.data)
        return Response(serializer.data)





class DistrictList(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (permissions.AllowAny, )

class DistrictDetail(APIView):

    def post(self, request):
        name = request.data.get('name')
        exist = District.objects.filter(name=name).exists()
        print(f"exist: {exist}")
        if exist: return Response()
        county = County.objects.get(id=request.data['related_model_name'])
        try:
            district = District.objects.create(name=name, county=county)
            create_polygon(request, district)
            print(f"district: {district}")
        except Exception as e:
            print(e)
        return Response()

    def get(self, request, *args, **kwargs):
        related_model_id = kwargs['related_model_id']
        districts = District.objects.filter(region_id=related_model_id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)

    


class NeighborhoodList(ListAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = (permissions.AllowAny, )

class NeighborhoodDetail(APIView):

    def post(self, request):
        polygon = create_polygon(request)
        district = District.objects.get(id=request.data['related_model_id'])
        try:
            neighborhood = Neighborhood.objects.create(name=request.data.get('name'), polygon=polygon, district=district)
            print(f"neighborhood: {neighborhood}")
        except Exception as e:
            print(e)
        return Response()
    
    def get(self, request, *args, **kwargs):
        related_model_id = kwargs['related_model_id']
        districts = District.objects.filter(region_id=related_model_id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


def create_polygon(request, model): 

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
            print(f"coordinate: {coor}")
            polygon.coordinate.add(coor.id)
            polygon.save()
            print(f"model: {model}")
            print(f"model.polygon: {model.polygon}")
            model.polygon.add(polygon.id)
        else:
            print(form.errors)
    # print(polygon)
    # return polygon

