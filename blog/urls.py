from django.urls import path
from .views import BlogPostAPIView, BlogPostDetailView

urlpatterns = [
    path("", BlogPostAPIView.as_view(), name="blogs"),
    path("<int:id>", BlogPostDetailView.as_view(), name="blog"),
]
