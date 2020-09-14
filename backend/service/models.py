from django.db import models

class Coordinate(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()



    


class Region(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.ManyToManyField(Coordinate, blank=True)

 

class City(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.ManyToManyField(Coordinate, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

class County(models.Model):
    name  = models.CharField(max_length=50)
    coordinates = models.ManyToManyField(Coordinate, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    coordinates = models.ManyToManyField(Coordinate, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
