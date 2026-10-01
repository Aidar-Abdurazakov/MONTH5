from django.db.models import Count, Avg
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    ProductReviewsSerializer
)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.annotate(
        products_count=Count('products')
    )
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProductReviewsListAPIView(ListAPIView):
    queryset = Product.objects.annotate(
        rating=Avg('reviews__stars')
    )
    serializer_class = ProductReviewsSerializer


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'