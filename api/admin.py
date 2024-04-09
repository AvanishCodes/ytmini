from django.contrib import admin
from .models import Channel, Video, YoutubeAPIKey

# Register your models here.
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(YoutubeAPIKey)