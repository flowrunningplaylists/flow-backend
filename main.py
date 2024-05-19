from combiner import Combiner
from cadence import StravaAPI, ActivityType
from dotenv import load_dotenv
from spotify import *
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

activity_type = ActivityType.RUN # will be dynamic value later

# strava
strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
if not strava.autheticateAndGetAllActivities():
    print("Error: probably out of access tokens for Strava's API")
    exit()
data = strava.getCadenceData(activity_type)
recent = strava.getRecentActivities()
print(recent)

# combiner
cb = Combiner(arrs=data)

combined_list = cb.combine()
print(combined_list)
print(len(cb.combine()))

# spotify
spotify = SpotifyAPI()
spotify.readDataAndAuthenticate()
spotify.get_top_songs_data()
spotify.add_to_queue()

# song_data = get_top_songs_data()
# add_to_queue(song_data)
