from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from red_squirrel_api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns =[
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]