
from django.urls import path
from .views import (
    RegionList,
    RegionDetail,
    CityList,
    CityDetail,
    CountyDetail,
    CountyList,
    NeighborhoodList,
    NeighborhoodDetail,

)

urlpatterns = [
    path('region/', RegionList.as_view()) ,
    path('region/post/', RegionDetail.as_view()),
    path('region/delete/<int:pk>/', RegionDetail.as_view()),
    path('city/', CityList.as_view()),
    path('city/post/', CityDetail.as_view()),
    path('city/get/<related_model_id>/', CityDetail.as_view()),
    path('county/', CountyList.as_view()),
    path('county/post/', CountyDetail.as_view()),
    path('county/get/<related_model_id>/', CountyDetail.as_view()),
    path('neighborhood/', NeighborhoodList.as_view()),
    path('neighborhood/post/', NeighborhoodDetail.as_view()),
    path('neighborhood/get/<related_model_id>/', NeighborhoodDetail.as_view()),

]