from django.db import models


class Coordinate(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()


class AbstractArea(models.Model):
    name = models.CharField(max_length=50)
    coordinate = models.ForeignKey(Coordinate, verbose_name='coordinate', on_delete=models.CASCADE, default=12)
   
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class Neighborhood(AbstractArea):
    pass

class District(AbstractArea):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,  related_name='district')

class Town(AbstractArea):
    district = models.ForeignKey(District, on_delete=models.CASCADE,  related_name='town')

class City(AbstractArea):
    town = models.ForeignKey(Town, on_delete=models.CASCADE,  related_name='city')

class Region(AbstractArea):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='region')

