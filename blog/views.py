from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import BlogPost
from .serializer import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import CustomPageNumberPagination

# Create your views here.


class BlogPostAPIView(ListCreateAPIView):
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = CustomPageNumberPagination
    filterset_fields = ["id", "title", "content"]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return BlogPost.objects.filter()


class BlogPostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = "id"
    def get_queryset(self):
        return BlogPost.objects.filter()
