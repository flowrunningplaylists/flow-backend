from combiner import Combiner
from cadence import StravaAPI
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
data = strava.getCadenceData()
cb = Combiner(arrs=data)

print(cb.combine())
pprint(len(cb.combine()))
