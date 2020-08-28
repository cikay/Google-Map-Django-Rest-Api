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
    name    = models.CharField(max_length=50)
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
 

class City(models.Model):
    name    = models.CharField(max_length=50)
    polygon = models.ForeignKey(Polygon,  on_delete=models.CASCADE)
    region  = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region')

class County(models.Model):
    name    = models.CharField(max_length=50)
    polygon = models.ForeignKey(Polygon,  on_delete=models.CASCADE)
    city    = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')

class District(models.Model):
    name    = models.CharField(max_length=50)
    polygon = models.ForeignKey(Polygon,  on_delete=models.CASCADE)
    town    = models.ForeignKey(County, on_delete=models.CASCADE, related_name='county')

class Neighborhood(models.Model):
    name        = models.CharField(max_length=50)
    polygon     = models.ForeignKey(Polygon,  on_delete=models.CASCADE)
    district    = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district')



