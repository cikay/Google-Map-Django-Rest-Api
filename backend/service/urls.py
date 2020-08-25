
from django.urls import path
from .views import (
   
    RegionList,
    RegionDetail,
    CityDetail,
    TownDetail,
    DistrictDetail,
    NeighborhoodDetail,

)

urlpatterns = [
    path('region/', RegionList.as_view()) ,
    path('region/detail/', RegionDetail.as_view()),
    path('region/<pk>/update/', RegionDetail.as_view()),
    path('city/detail/', CityDetail.as_view()),
    path('town/detail/', TownDetail.as_view()),
    path('district/detail/', DistrictDetail.as_view()),



    # path('city/', CityListCreateView.as_view()),
    # path('town/', TownListCreateView.as_view()),
    # path('district/', DistrictListCreateView.as_view()),
    # path('neigborhood/', NeighborhoodListCreateView.as_view()),
   
]