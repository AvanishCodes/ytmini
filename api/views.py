from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Video, Channel
from .serializers import VideoSerializer
from .pagination import DefaultPagination


class SearchVideosAPIView(APIView):
    # Add params to the decorator
    @swagger_auto_schema(
        operation_description="List all stored videos",
        manual_parameters=[
            openapi.Parameter(
                "title",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Filter by title",
            ),
            openapi.Parameter(
                "description",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Filter by description",
            ),
            openapi.Parameter(
                "skip",
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Skip the first N videos",
            ),
            openapi.Parameter(
                "limit",
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=False,
                description="Limit the number of videos returned",
            ),
        ],
        responses={200: "Hello, world. This is the list videos API!"},
    )
    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        title = params.get("title")
        description = params.get("description")
        skip = params.get("skip") or 0
        limit = params.get("limit")
        if limit:
            limit = int(limit)
        else:
            limit = 10
        videos = Video.objects.all().order_by("-published_at")
        if title:
            videos = videos.filter(title__icontains=title)
        if description:
            videos = videos.filter(description__icontains=description)
        if skip:
            videos = videos[int(skip):]
        videos = videos[:limit]
        return Response(VideoSerializer(videos, many=True).data)

class ListVideosAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = DefaultPagination

__all__ = [
    "SearchVideosAPIView",
    "ListVideosAPIView",
]
