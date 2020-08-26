
from django.urls import path
from .views import (
   
    RegionList,
    RegionDetail,
    CityDetail,
    CountyDetail,
    DistrictDetail,
    NeighborhoodDetail,

)

urlpatterns = [
    path('region/', RegionList.as_view()) ,
    path('region/detail/', RegionDetail.as_view()),
    path('region/<pk>/update/', RegionDetail.as_view()),
    path('city/detail/', CityDetail.as_view()),
    path('town/detail/', CountyDetail.as_view()),
    path('district/detail/', DistrictDetail.as_view()),
    path('neighborhood/detail/', NeighborhoodDetail.as_view()),

   
]