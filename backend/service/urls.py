
from django.urls import path
from .views import (
    NeighborhoodDetail,
    RegionList,
    RegionDetail,
    CityDetail,
    
)

urlpatterns = [
    path('region/', RegionList.as_view()) ,
    path('region/detail/', RegionDetail.as_view()),
    path('region/<pk>/update/', RegionDetail.as_view()),
    path('city/detail/', CityDetail.as_view())
    # path('city/', CityListCreateView.as_view()),
    # path('town/', TownListCreateView.as_view()),
    # path('district/', DistrictListCreateView.as_view()),
    # path('neigborhood/', NeighborhoodListCreateView.as_view()),
   
]