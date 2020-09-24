from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from fizzbuzz.views import CategoryViewSet, SubCategoryViewSet


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]