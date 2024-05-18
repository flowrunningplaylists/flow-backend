from combiner import Combiner
from cadence import StravaAPI

strava = StravaAPI(
    client_id='126930', 
    client_secret='a8f24465f2e64522b1205955dfbd088c0a706188', 
    redirect_uri='http://localhost'
)
data = strava.getCadenceData()
cb = Combiner(arrs=data)

print(cb.combine())
print(len(cb.combine()))
