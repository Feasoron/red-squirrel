from rest_framework import serializers
from red_squirrel.models import Food, Category, Unit, StorageLocation

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StorageLocation
        fields = ('url', 'name')

class UnitSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Unit
        fields = ('url', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Category
        fields = ('url', 'name')

class FoodSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Food
        fields = ('url', 'name', 'category', 'location')
