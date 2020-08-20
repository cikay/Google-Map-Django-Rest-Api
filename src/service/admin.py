from django.contrib import admin

from .models import (
    Coordinate,
    Region,
    City,
    Town,
    District,
    Neighborhood
)
admin.site.register(Coordinate)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Town)
admin.site.register(District)
admin.site.register(Neighborhood)
