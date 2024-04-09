from rest_framework.serializers import ModelSerializer
from .models import Video, Channel

class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

__all__ = [
    "ChannelSerializer",
    "VideoSerializer",
]