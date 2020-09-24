from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import status
from fizzbuzz.serializer import (
    CategorySerializer,
    SubCategorySerializer
)
from fizzbuzz.models import Category, SubCategory
from .utils import CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination



class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CustomPagination
