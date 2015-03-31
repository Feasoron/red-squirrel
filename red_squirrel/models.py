from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class StorageLocation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Conversion(models.Model):
    firstUnit = models.ForeignKey(Unit, related_name='first_unit')
    secondUnit = models.ForeignKey(Unit, related_name='second_unit')
    ratio = models.FloatField()

class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    # If we break food up, so you can have multiple inventories of a food type
    # this is a natural breaking point

    location = models.ForeignKey(StorageLocation)
    quantity = models.IntegerField(default=1)
    unit = models.ForeignKey(Unit)
    best_by = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

