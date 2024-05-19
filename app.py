from flask import Flask, request, jsonify
from combiner import Combiner
from cadence import StravaAPI
from dotenv import load_dotenv
from spotify import *
import os

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')

strava = StravaAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
strava.autheticateAndGetAllActivities()
# cadence_data = strava.getCadenceData()

app = Flask(__name__)

@app.route('/api/demo', methods=['GET'])
def demo():
    return "Welcome The Flow API"

@app.route('/recent', methods=['GET'])
def getRecent():
    # Call something like stava.getRecent() and return a json
    json = jsonify(strava.getRecentActivities())
    return json

@app.route('/playlist', methods=['GET'])
def getPlaylist():
    activity = request.args.get('activity')
    # call like get playlist or somthing bs


    

@app.route('/api/greeting', methods=['POST'])
def getData():
    data = request.get_json()
    name = data.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
    