from django.db import models

class Coordinate(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()


class Polygon(models.Model):
    coordinate = models.ManyToManyField(Coordinate, blank=True)

class AbstractArea(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.ManyToManyField(Polygon, verbose_name='polygon', blank=True)
   
    def __str__(self):
        
        return self.name
    
    class Meta:
        abstract = True


class Region(AbstractArea):
    pass

class City(AbstractArea):
    region = models.ForeignKey(Region, on_delete=models.CASCADE,  related_name='city', blank=True)

class Town(AbstractArea):
    city = models.ForeignKey(City, on_delete=models.CASCADE,  related_name='town')

class District(AbstractArea):
    town = models.ForeignKey(Town, on_delete=models.CASCADE,  related_name='district')

class Neighborhood(AbstractArea):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='neighborhood')



