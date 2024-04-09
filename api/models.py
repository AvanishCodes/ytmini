from django.db import models
import hashlib

# Create your models here.

class Channel(models.Model):
    channel_id = models.CharField(max_length=24)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_id = models.CharField(max_length=11)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class YoutubeAPIKey(models.Model):
    key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # While displaying the object, display the hash of the key to avoid leaking the key
        return hashlib.sha256(self.key.encode()).hexdigest()
    
__all__ = ["Channel", "Video"]