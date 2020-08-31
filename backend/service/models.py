from django.db import models

class Coordinate(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Polygon(models.Model):
    coordinate = models.ManyToManyField(Coordinate, blank=True)

    
# class AbstractArea(models.Model):
#     name = models.CharField(max_length=50)
#     polygon = models.ForeignKey(Polygon,  on_delete=models.CASCADE)
   
#     def __str__(self):
        
#         return self.name
    
#     class Meta:
#         abstract = True


class Region(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, blank=True)
 

class City(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

class County(models.Model):
    name  = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

class District(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)



