from time import sleep
import spotipy  
from spotipy.oauth2 import SpotifyOAuth  
import json

CLIENT_ID="5c17cfd2c3884a6aa0b8d92d21ccf51e"
CLIENT_SECRET="ce4bd0c559f149aeb281ecfd8d84da9b"
REDIRECT_URI="http://localhost:3000"
SCOPE = "user-library-read, user-modify-playback-state, user-read-playback-state, user-top-read"
BPM_UNCERTAINTY = 3
CADENCE_INTERVAL_SEC = 3.43

sample_cadence_data = []

# Read JSON file and assign to variable
with open('combined.txt', 'r') as file:
    sample_cadence_data = json.load(file)

# authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))


def get_cadence_avg(start_time, duration):
    start_index = int(start_time/CADENCE_INTERVAL_SEC)
    end_index = int (start_time + int(duration/CADENCE_INTERVAL_SEC))
    print("start index", start_index, "end_index", end_index)

    total = sum(sample_cadence_data[i] for i in range(start_index, end_index))
    count = end_index - start_index

    average = total / count
    return average

def get_top_songs_data(num_songs=10):
    data = {}

    results = sp.current_user_top_tracks(limit=num_songs, offset=0, time_range='medium_term')
    for idx, item in enumerate(results['items']):
        id = item['id']
        name = item['name']
        duration = round(item['duration_ms']/1000, 2)
        uri = item['uri']

        data[id] = {"name" : name, "duration" : duration, "uri" : uri}
    
        print(idx+1, name, duration, id, uri) 

    # bpm_arr = []
    # running_bpm_arr = []
    for id in data:
        result = sp.audio_analysis(track_id=id)
        bpm = result['track']['tempo']
        data[id]['bpm'] = bpm
        print(bpm)
        
        # double it if it is too low
        running_bpm = bpm
        if bpm < 110:
            running_bpm *= 2
        
        # running_bpm_arr.append(running_bpm)
        # bpm_arr.append(bpm)
        data[id]['running_bpm'] = running_bpm
    
    return data

# avg_cadence = round(sum(sample_cadence_data)/len(sample_cadence_data)*2, 2)
# print(avg_cadence)


def add_to_queue(song_data):
    time_elapsed_sec = 0 # total duration of songs played

    while(True): # todo fix
        target_spm = round(get_cadence_avg(time_elapsed_sec, 200) * 2, 2)
        print("Target spm:", target_spm)

        closest_entry = min(song_data.items(), key=lambda item: abs(item[1]['running_bpm'] - target_spm))
        print(closest_entry)

        print("\nError:", abs(closest_entry[1]['running_bpm'] - target_spm), "\n")

        # add a song to queue
        sp.add_to_queue(uri=closest_entry[1]['uri']) # todo set default device when no active device is detected
        print(f"Added {closest_entry[1]['name']} to queue")

        del song_data[closest_entry[0]]

        time_elapsed_sec += closest_entry[1]['duration']
        print("Current length of queue (sec):", round(time_elapsed_sec, 2))

        sleep(10) # todo fix

add_to_queue()