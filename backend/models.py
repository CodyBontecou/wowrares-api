''' Database models Item, Zone, and Mob. '''

from django.db import models
from django.urls import reverse


class Zone(models.Model):
    '''
    Object representing the zone that each mob resides in
    '''
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        ''' Method that returns the Zone object's url pattern. '''
        return reverse('zone', kwargs=self.name)


class Mob(models.Model):
    '''
    Object representing each rare mob that resides within a zone.
    '''
    name = models.CharField(max_length=255, blank=True)
    image = models.TextField(blank=True)
    level = models.CharField(max_length=2)
    health = models.CharField(max_length=255, blank=True)
    damage = models.CharField(max_length=255, blank=True)
    armor = models.CharField(max_length=255, blank=True)
    model_id = models.CharField(max_length=255, blank=True)
    faction = models.CharField(max_length=255, blank=True)
    x_coordinate = models.CharField(max_length=255, blank=True)
    y_coordinate = models.CharField(max_length=255, blank=True)
    coordinates = models.CharField(max_length=255, blank=True)
    zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', blank=True)
    websites_id = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    '''
    Object representing the items that drop off of a mob
    '''
    drop_rate = models.CharField(max_length=255, blank=True)
    i_level = models.CharField(max_length=255, blank=True)
    image = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    required_level = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
