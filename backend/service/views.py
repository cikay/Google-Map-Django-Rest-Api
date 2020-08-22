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


class RegionUpdate(APIView):
 
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
    


