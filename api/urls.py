from django.urls import path

from .views import ListVideosAPIView, SearchVideosAPIView

urlpatterns = [
    path("search", SearchVideosAPIView.as_view(), name="list-videos"),
    path("list", ListVideosAPIView.as_view(), name="search-videos"),
]
