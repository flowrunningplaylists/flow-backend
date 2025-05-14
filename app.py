from flask import Flask, request, jsonify, redirect
from combiner import Combiner
from cadence import *
from dotenv import load_dotenv
from spotify import *
import os

haha = None

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
CLIENT_ID_SPOTIFY = os.getenv('CLIENT_ID_SPOTIFY')
CLIENT_SECRET_SPOTIFY=os.getenv('CLIENT_SECRET_SPOTIFY')
REDIRECT_URI_SPOTIFY=os.getenv('REDIRECT_URI_SPOTIFY')

app = Flask(__name__)

strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
spotify = SpotifyAPI(CLIENT_ID_SPOTIFY, CLIENT_SECRET_SPOTIFY, REDIRECT_URI_SPOTIFY)
print(spotify.sp == None)
# print(spotify.CLIENT_ID_SPOTIFY, CLIENT_SECRET_SPOTIFY, REDIRECT_URI_SPOTIFY)
strava.autheticateAndGetAllActivities()
# cadence_data = strava.getCadenceData()



REDIRECT_URI_temp = 'https://hawkhacks2024.onrender.com/callback'

#step 2
@app.route('/login')
def login():
    auth_url = (
        f'https://www.strava.com/oauth/authorize'
        f'?client_id={CLIENT_ID}'
        f'&redirect_uri={REDIRECT_URI_temp}'
        f'&response_type=code'
        f'&scope=activity:read_all'
    )
    return redirect(auth_url)

#step 1
# @app.route('/loginspotify')
# def loginspotify():
#     spotify.auth()
#     # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY, client_secret=CLIENT_SECRET_SPOTIFY, redirect_uri=REDIRECT_URI_SPOTIFY, scope=spotify.SCOPE))
#     # spotify.sp = sp
#     # auth_url = (
#     #     f'https://www.strava.com/oauth/authorize'
#     #     f'?client_id={CLIENT_ID}'
#     #     f'&redirect_uri={REDIRECT_URI_temp}'
#     #     f'&response_type=code'
#     #     f'&scope=activity:read_all'
#     # )
#     return jsonify('authspotify')

#follows from step 2
@app.route('/callback')
def callback():
    code = request.args.get('code')

    #strava auth
    strava.autheticateAndGetAllActivities(code)
    data = strava.getCadenceData(ActivityType.RUN)
    print(data)
    #combiner
    cb = Combiner(arrs=data)
    combined_list = cb.combine()
    print("from strava combined", combined_list)
    # spotify
    spotify.load_cadence_data(combined_list)
    print("from txt", spotify.cadence_data)
    return jsonify(code)

#will never be called
@app.route('/callbackspotify')
def callbackspotify():
    return jsonify('callbackspotify')


@app.route('/api/demo', methods=['GET'])
def demo():
    return "Welcome The Flow API"

@app.route('/recent', methods=['GET'])
def getRecent():
    # Call something like stava.getRecent() and return a json
    json = jsonify(strava.getRecentActivities())
    return json
    # return jsonify("Troll")

@app.route('/start', methods=['GET'])
def start():
    spotify.get_top_songs_data()
    spotify.add_to_song_list()
    print('0',spotify.generated_song_list)
    return jsonify(spotify.generated_song_list)
    # return "200"

@app.route('/addtoqueue', methods=['GET'])
def add_to_queue():
    spotify.add_songs_to_queue()
    return "200"

@app.route('/createplaylist', methods=['GET'])
def create_playlist():
    spotify.create_playlist()    
    return "200"

@app.route('/playlist', methods=['GET'])
def getPlaylist():
    # activity = request.args.get('activity')
    print('1',spotify.get_generated_song_list())
    print('2',spotify.generated_song_list)
    json = jsonify(spotify.generated_song_list)
    print(haha)
    return haha

@app.route('/plot', methods=['GET'])
def getPlot():
    # gets the plot for a playlist ig
    pass

@app.route('/api/greeting', methods=['POST'])
def getData():
    data = request.get_json()
    name = data.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001) 
    