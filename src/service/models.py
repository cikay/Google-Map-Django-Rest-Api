from django.db import models


class Coordinate(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()


class AbstractArea(models.Model):
    name = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True


class Region(AbstractArea):
    
    coordinates = models.ManyToManyField(Coordinate, verbose_name='coordinates', related_name='region')
    
    # test = models.CharField(max_length=20, default='string')


class City(AbstractArea):
   region = models.ForeignKey(Region, verbose_name='region', on_delete=models.CASCADE, related_name='city')

class Town(AbstractArea):
    city = models.ForeignKey(City, verbose_name='city', on_delete=models.CASCADE, related_name='town')


class District(AbstractArea):
    town = models.ForeignKey(Town, verbose_name='town',on_delete=models.CASCADE,  related_name='district')


class Neighborhood(AbstractArea):
    district = models.ForeignKey(District, verbose_name='district',on_delete=models.CASCADE,  related_name='neighborhood')



# class District(models.Model):
#     name = models.CharField(max_length=50)
#     coordinates = models.ManyToManyField(Coordinate, verbose_name='coordinate')

# class County(models.Model):
#     name = models.CharField(max_length=50)
#     coordinates = models.ManyToManyField(Coordinate, verbose_name='coordinate')


# class City(models.Model):
#     name = models.CharField(max_length=50)
#     coordinates = models.ManyToManyField(Coordinate, verbose_name='coordinate')
#     county = models.ManyToManyField(County,on_delete=models.CASCADE,verbose_name='sehirler)



# class Region(models.Model):
#     name = models.CharField(max_length=50)
#     coordinates = models.ManyToManyField(Coordinate,on_delete=models.CASCADE, verbose_name='coordinate')
#     city = models.ManyToManyField(City,on_delete=models.CASCADE,verbose_name='sehirler)
