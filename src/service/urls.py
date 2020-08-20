
from django.urls import path
from .views import (
    RegionListCreateView,
    CityListCreateView,
    TownListCreateView,
    DistrictListCreateView,
    NeighborhoodListCreateView
)

urlpatterns = [
    path('region/', RegionListCreateView.as_view()),
    path('city/', CityListCreateView.as_view()),
    path('town/', TownListCreateView.as_view()),
    path('district/', DistrictListCreateView.as_view()),
    path('neigborhood/', NeighborhoodListCreateView.as_view()),
   
]