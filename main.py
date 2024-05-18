from combiner import Combiner
from cadence import StravaAPI, ActivityType
from dotenv import load_dotenv
from spotify import *
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

activity_type = ActivityType.RUN # user can choose any activity

strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
data = strava.getCadenceData(activity_type)
cb = Combiner(arrs=data)

combined_list = cb.combine()
print(combined_list)
print(len(cb.combine()))

song_data = get_top_songs_data()
add_to_queue(song_data)
