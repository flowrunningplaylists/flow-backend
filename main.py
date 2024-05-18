from combiner import Combiner
from cadence import StravaAPI, ActivityType
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

activity_type = ActivityType.RUN # user can choose any activity

strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
data = strava.getCadenceData(activity_type)
cb = Combiner(arrs=data)

print(cb.combine())
print(len(cb.combine()))
