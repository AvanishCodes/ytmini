# Native Python Imports
import logging
from time import sleep
from random import choice
from datetime import datetime as dt, timedelta as td, timezone as tz

# PyPI Imports
from googleapiclient.discovery import build

# Local Imports
from api.models import Video, YoutubeAPIKey, Channel

start_time:  dt = dt.now(tz=tz.utc)
current_time: dt = start_time
TOPIC = "IPL 2024" # At the time of writing this script, IPL 2024 is a trending topic

while True:
    try:
        # Fetch the youtube videos released in the last 1 minute
        yt_videos: list[dict] = []
        to_timestamp = current_time.isoformat()
        from_timestamp = (current_time - td(minutes=1)).isoformat()

        keys = YoutubeAPIKey.objects.all()
        # Choose a random API key
        key = choice(keys)
        yt_obj = build("youtube", "v3", developerKey=key.key)

        results = yt_obj.search().list(q=TOPIC, part="id, snippet", maxResults=10, publishedAfter=from_timestamp, publishedBefore=to_timestamp).execute()
        yt_videos = [
            {
                "title": item["snippet"]["title"],
                "video_id": item["id"]["videoId"],
                "channel": Channel.objects.get_or_create(title=item["snippet"]["channelTitle"], channel_id=item["snippet"]["channelId"])[0],
                "description": item["snippet"]["description"],
                "published_at": item["snippet"]["publishedAt"],
            }
            for item in results["items"]
        ]
        logging.info(f"Fetched {len(yt_videos)} videos at {current_time}")

        # Save the fetched videos to the database
        for video in yt_videos:
            # Check if the channel exists in the database
            Video.objects.create(
                title=video["title"],
                video_id=video["video_id"],
                channel=video["channel"],
                description=video["description"],
                published_at=video["published_at"],
            )
        sleep(10)
    except Exception as e:
        print(f"Error: {e} at {current_time}")
    
    current_time = current_time + td(seconds=10)
