import requests
import webbrowser
from pprint import pprint

# Step 1: Set up your Strava API application credentials
CLIENT_ID = '126930'
CLIENT_SECRET = 'a8f24465f2e64522b1205955dfbd088c0a706188'
REDIRECT_URI = 'http://localhost'  # Your redirect URI
AUTH_URL = 'https://www.strava.com/oauth/authorize'
TOKEN_URL = 'https://www.strava.com/oauth/token'

# Step 2: Obtain the authorization code
params = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'response_type': 'code',
    'scope': 'activity:read_all'
}
auth_request = requests.Request('GET', AUTH_URL, params=params).prepare()
auth_url = auth_request.url
print(f'Opening the following URL in your browser: {auth_url}')
webbrowser.open(auth_url)

# Step 3: User authorizes and we get the authorization code from the redirect URL
print('Please authorize the app and paste the full redirect URL here:')
redirect_response = input('> ')
auth_code = redirect_response.split('code=')[1].split('&')[0]

# Step 4: Exchange authorization code for access token
token_params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': auth_code,
    'grant_type': 'authorization_code'
}
response = requests.post(TOKEN_URL, data=token_params)
tokens = response.json()
access_token = tokens['access_token']

# Step 5: Make an API call to get the athlete's activities
activities_url = 'https://www.strava.com/api/v3/athlete/activities'
headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'per_page': 30,
    'page': 1
}
activities_response = requests.get(activities_url, headers=headers, params=params)
activities = activities_response.json()
pprint(activities)
if activities['errors']:
    pprint("Rate Limit has probably been exceeded. Exiting now.")
    exit()


# step 6: extract activity ids
activityIds = []
if activities:
    for activity in activities:
        activityIds.append(activity['id'])

# step 7: make API calls to get activity streams
max_requests = 3; # to prevent ourselves from going over Strava's imposed limit
n = 0
for activityId in activityIds:
    if n > max_requests:
        break
    activitiesStream_url = 'https://www.strava.com/api/v3/activities/' + str(activityId) + '/streams'
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = { #StreamSet get_activity_streams(id, keys, key_by_type)
        'id': activityId,
        'keys': ['cadence'],
        'key_by_type': True
    }
    pprint(activitiesStream_url)
    activitiesStream_response = requests.get(activitiesStream_url, headers=headers, params=params)
    n += 0

    activitiesStream = activitiesStream_response.json()
    pprint(activitiesStream)

# ----
# Step 6: Print the data
# pprint(activityIds)

# if activities:
#     for activity in activities:
#         print(f"Activity ID: {activity['id']}")
#         print(f"Name: {activity['name']}")
#         print(f"Distance: {activity['distance']} meters")
#         print(f"Type: {activity['type']}")
#         print(f"Moving Time: {activity['moving_time']} seconds")
#         print(f"Elapsed Time: {activity['elapsed_time']} seconds")
#         print(f"Total Elevation Gain: {activity['total_elevation_gain']} meters")
#         print(f"Average Cadence: {activity['average_cadence']} rotations per minute")
#         print()  # Print a blank line for readability
