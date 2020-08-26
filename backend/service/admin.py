from django.contrib import admin

from .models import (
    Coordinate,
    Region,
    City,
    County,
    District,
    Neighborhood
)
admin.site.register(Coordinate)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(County)
admin.site.register(District)
admin.site.register(Neighborhood)
