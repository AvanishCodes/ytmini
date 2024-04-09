import json
from googleapiclient.discovery import build
from datetime import datetime as dt, timedelta as td, timezone as tz

MAX_RESULTS = 10
KEYWORD = "IPL 2024"
API_KEY = "AIzaSyDd65m_bmigbqPzGCYa_zOBWlDUP_UbOQU"
# Fetch the youtube videos released in the last 10 seconds

yt_obj = build("youtube", "v3", developerKey=API_KEY)
current_time = dt.now(tz=tz.utc)
time_before_1_hour = current_time - td(hours=1)


results = yt_obj.search().list(q=KEYWORD, part="id, snippet", maxResults=MAX_RESULTS, publishedAfter=time_before_1_hour.isoformat()
                               ).execute()
# Save the fetched videos to the JSON file
with open("yt.json", "w") as f:
    json.dump(results, f)