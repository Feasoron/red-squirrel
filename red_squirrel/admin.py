from django.contrib import admin
from red_squirrel.models import StorageLocation, Category, Unit, Food

# Register your models here.
admin.site.register(StorageLocation)
admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Food)