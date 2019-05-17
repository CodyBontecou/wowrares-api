''' Database models Item, Zone, and Mob. '''

from django.db import models
from django.urls import reverse


class Zone(models.Model):
    '''
    Object representing the zone that each mob resides in
    '''
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True)
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
    name = models.TextField(blank=True)
    image = models.TextField(blank=True)
    level = models.TextField(blank=True)
    health = models.TextField(blank=True)
    damage = models.TextField(blank=True)
    armor = models.TextField(blank=True)
    model_id = models.TextField(blank=True)
    faction = models.TextField(blank=True)
    x_coordinate = models.TextField(blank=True)
    y_coordinate = models.TextField(blank=True)
    coordinates = models.TextField(blank=True)
    zone = models.ForeignKey('Zone', on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', blank=True)
    websites_id = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    '''
    Object representing the items that drop off of a mob
    '''
    drop_rate = models.TextField(blank=True)
    i_level = models.TextField(blank=True)
    image = models.TextField(blank=True)
    name = models.TextField(blank=True)
    required_level = models.TextField(blank=True)
    type = models.TextField(blank=True)

    def __str__(self):
        return self.name
