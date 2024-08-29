
from django.contrib import admin
from django.urls import path

from texnomart_uz.views import ProductListView, CategoryListView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, CategoryDetailView, ProductCreateView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, KeyListView, ValueListView, ProductCategoryView

urlpatterns = [
    # Views for Products
    path('', ProductListView.as_view(), name='product-list'),
    path('category/<slug:category_slug>/', ProductCategoryView.as_view()),
    path('product/add-product/', ProductCreateView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view()),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view()),

    # ------------------------------------------------------------ #
    # Views for Categories
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/add-category/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<slug:slug>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # Key LIst View
    path('attribute-key/', KeyListView.as_view(), name='attribute-key'),
    # Value List View
    path('attribute-value/', ValueListView.as_view(), name='attribute-value'),



]
