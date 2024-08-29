import rest_framework_simplejwt
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from rest_framework import generics, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from texnomart_uz.models import Product, Category, Key
from texnomart_uz.serializers import ProductSerializer, CategorySerializer, KeySerializer, ValueSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['category', 'price', 'is_liked']
    search_fields = ['name', 'description']

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductCategoryView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = get_object_or_404(Category, slug=category_slug)
        queryset = Product.objects.filter(category=category)
        return queryset

    lookup_field = 'slug'

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'pk'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'slug'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'slug'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    lookup_field = 'slug'
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication


class KeyListView(generics.ListAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ValueListView(generics.ListAPIView):
    queryset = Key.objects.all()
    serializer_class = ValueSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]  # authentication.TokenAuthentication

    @method_decorator(cache_page(60 * 3))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
