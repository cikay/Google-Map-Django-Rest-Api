
from django.urls import path
from .views import (
    NeighborhoodDetail,
    RegionList,
    RegionUpdate,
    
)

urlpatterns = [
    path('neighborhood/', )
    path('region/', RegionList.as_view()),
    path('region/<pk>/update/', RegionUpdate.as_view()),
    # path('city/', CityListCreateView.as_view()),
    # path('town/', TownListCreateView.as_view()),
    # path('district/', DistrictListCreateView.as_view()),
    # path('neigborhood/', NeighborhoodListCreateView.as_view()),
   
]
    