from rest_framework import viewsets
from red_squirrel.models import Food, Category, Unit, StorageLocation
from red_squirrel_api.serializers import FoodSerializer, CategorySerializer, LocationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer