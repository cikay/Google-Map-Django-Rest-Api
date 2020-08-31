
from django.urls import path
from .views import (
   
    RegionList,
    RegionDetail,
    CityList,
    CityDetail,
    CountyDetail,
    CountyList,
    DistrictList,
    DistrictDetail,
    NeighborhoodList,
    NeighborhoodDetail,

)

urlpatterns = [
    path('region/', RegionList.as_view()) ,
    path('region/detail/', RegionDetail.as_view()),
    path('city/', CityList.as_view()),
    path('city/detail/', CityDetail.as_view()),
    path('city/<related_model_id>/', CityDetail.as_view()),
    path('county/', CountyList.as_view()),
    path('county/<related_model_id>/', CountyDetail.as_view()),
    path('county/detail/', CountyDetail.as_view()),
    path('district/', DistrictList.as_view()),
    path('district/detail/', DistrictDetail.as_view()),
    path('neighborhood/', NeighborhoodList.as_view()),
    path('neighborhood/detail/', NeighborhoodDetail.as_view()),

]