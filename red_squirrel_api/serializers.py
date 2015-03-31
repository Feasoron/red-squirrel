from rest_framework import serializers
from red_squirrel.models import Food, Category, Unit, StorageLocation

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StorageLocation
        fields = ('name')

class UnitSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Unit
        fields = ('name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Category
        fields = ('name')

class FoodSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Food
        fields = ('name', 'category', 'location')
