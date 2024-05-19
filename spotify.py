from time import sleep
import spotipy  
from spotipy.oauth2 import SpotifyOAuth  
import json


class SpotifyAPI:
    def __init__(self, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):
        # self.CLIENT_ID="5c17cfd2c3884a6aa0b8d92d21ccf51e"
        # self.CLIENT_SECRET="ce4bd0c559f149aeb281ecfd8d84da9b"
        # self.REDIRECT_URI="http://localhost:3000"
        self.CLIENT_ID=CLIENT_ID
        self.CLIENT_SECRET=CLIENT_SECRET
        self.REDIRECT_URI=REDIRECT_URI
        self.SCOPE = "user-library-read, user-modify-playback-state, user-read-playback-state, user-top-read, user-read-email, user-read-private, playlist-modify-public, playlist-modify-private"
        self.BPM_UNCERTAINTY = 3
        self.CADENCE_INTERVAL_SEC = 3.43
        self.ERROR_THRESHOLD = 10
        self.BPM_THRESHOLD = 110
        self.LOUDNESS_DROP_THRESHOLD = -4
        self.NUM_TOP_SONGS = 10
        self.SONG_LIST_LEN = 3

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI, scope=self.SCOPE))
        self.cadence_data = None
        self.song_data = {}
        self.device_id = None
        self.device_is_active = False
        self.playback_progress_sec = 0
        self.is_playing = False
        self.current_id = None
        self.seed_tracks = []
        self.seed_genre = []
        self.seed_artist = []
        self.generated_song_list = {}

        # self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI, scope=self.SCOPE))

    # def auth(self):
    #     self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI, scope=self.SCOPE))


    def load_cadence_data(self, cadence_data):
        # testing
        # Read JSON file and assign to variable
        with open('combined.txt', 'r') as file:
            self.cadence_data = json.load(file)
        # self.cadence_data = cadence_data
        print(self.cadence_data)

        #authenticate
        # self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI, scope=self.SCOPE))

        #populate seed_genre and seed_artist
        self.seed_artist.append(self.sp.current_user_top_artists(limit=1, offset=0, time_range='medium_term')['items'][0]['id'])
        self.seed_genre.append(self.sp.current_user_top_artists(limit=1, offset=0, time_range='medium_term')['items'][0]['genres'][0])

    def get_cadence_avg(self, start_time, duration):
        start_index = int(start_time/self.CADENCE_INTERVAL_SEC)
        end_index = int (start_time + int(duration/self.CADENCE_INTERVAL_SEC))
        print("start index", start_index, "end_index", end_index)
        print("in get_cadence_avg, print self.cadence_data", print(self.cadence_data))
        print(len(self.cadence_data))
        total = sum(self.cadence_data[i] for i in range(start_index, end_index))
        count = end_index - start_index

        average = total / count
        return average
    
    def get_user_devices(self):
        return self.sp.devices()

    def get_top_songs_data(self):

        results = self.sp.current_user_top_tracks(limit=self.NUM_TOP_SONGS, offset=0, time_range='medium_term')
        for idx, item in enumerate(results['items']):
            id = item['id']
            name = item['name']
            duration = round(item['duration_ms']/1000, 2)
            uri = item['uri']
            artist = [artist["name"] for artist in item['artists']]
            image = [image['url'] for image in item['album']['images']]

            self.song_data[id] = {"name" : name, "duration" : duration, "uri" : uri, 'image' : image, "artist" : artist}
    
            if idx < 3:
                self.seed_tracks.append(str(id))

            print(idx+1, name, duration, id, uri) 

        # print("seed_tracks: " + self.seed_tracks)

        for id in self.song_data:
            try:
                result = self.sp.audio_analysis(track_id=id)
            except Exception as e:
                print("An error occured", e)

            bpm = result['track']['tempo']
            self.song_data[id]['bpm'] = bpm
            print(bpm)
            
            # double it if it is too low
            running_bpm = bpm
            if bpm < self.BPM_THRESHOLD:
                running_bpm *= 2
            
            # running_bpm_arr.append(running_bpm)
            # bpm_arr.append(bpm)
            self.song_data[id]['running_bpm'] = running_bpm
        
        return self.song_data
    
    def add_recommended_songs(self):
        new_songs = {}

        results = self.sp.recommendations(seed_artists=self.seed_artist, seed_genres=self.seed_genre, seed_tracks=self.seed_tracks)

        for idx, item in enumerate(results['tracks']):
            id = item['id']
            name = item['name']
            duration = round(item['duration_ms']/1000, 2)
            uri = item['uri']
            artist = [artist["name"] for artist in item['artists']]
            image = [image['url'] for image in item['album']['images']]

            new_songs[id] = {"name" : name, "duration" : duration, "uri" : uri, 'image' : image, "artist" : artist}
            
            print("ADDED", idx+1, name, duration, id, uri) 

        for id in new_songs:
            try:
                result = self.sp.audio_analysis(track_id=id)
            except Exception as e:
                print("An error occured", e)

            bpm = result['track']['tempo']
            new_songs[id]['bpm'] = bpm
            print(bpm)
            
            # double it if it is too low
            running_bpm = bpm
            if bpm < self.BPM_THRESHOLD:
                running_bpm *= 2
            
            # running_bpm_arr.append(running_bpm)
            # bpm_arr.append(bpm)
            new_songs[id]['running_bpm'] = running_bpm
            # sleep(10)
        
        self.song_data.update(new_songs)
        
        return self.song_data


    def add_to_song_list(self):
        time_elapsed_sec = 0 # total duration of songs played

        while(len(self.generated_song_list) <= self.SONG_LIST_LEN): 
            target_spm = round(self.get_cadence_avg(time_elapsed_sec, 200) * 2, 2)
            print("Target spm:", target_spm)

            print("TEST",self.song_data)

            closest_entry = min(self.song_data.items(), key=lambda item: abs(item[1]['running_bpm'] - target_spm))
            print(closest_entry)
            
            song_id = closest_entry[0]
            song_attributes = closest_entry[1]
            error = abs(song_attributes['running_bpm'] - target_spm)

            print("\nError:", error, "\n")

            if error > self.ERROR_THRESHOLD:
                print('below error threshold')

                self.add_recommended_songs()

            else:
                # add a song to generated list
                self.generated_song_list[song_id] = {
                    'name': song_attributes['name'],
                    'artist': song_attributes['artist'],
                    'image': song_attributes['image'],
                    'length': song_attributes['duration'],
                    'bpm': song_attributes['bpm'],
                    'running_bpm': song_attributes['running_bpm'],
                    'uri': song_attributes['uri']
                }
                print(f"Added {song_attributes['name']} to generated list")

                # remove the song from original list after it's been added
                del self.song_data[song_id]

                time_elapsed_sec += song_attributes['duration']
                print("Current length of queue (sec):", round(time_elapsed_sec, 2))

            # sleep(10) 


    def add_songs_to_queue(self):
        for song_id in self.generated_song_list:
            self.sp.add_to_queue(uri=self.generated_song_list[song_id]['uri']) # todo set default device when no active device is detected (nvm too hard)
            print(f"Added {self.generated_song_list[song_id]['name']} to queue")


    def create_playlist(self, playlist_name='My awesome running playlist'):
        print("Creating playlist")
        user_id = self.sp.current_user()['id']
        result = self.sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
        playlist_id = result['id']
        self.sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=self.generated_song_list.keys())


    def get_generated_song_list(self):
        return self.generated_song_list

    # given sections array of a song, returns sections where there is a suddenly decrease in loudness
    def get_loudness_drop_sections(self, sections):
        if len(sections) < 1:
            return None
        
        print(type(sections))
        prev = sections[0]['loudness']
        res = []

        for section in sections:
            if section['loudness'] - prev < self.LOUDNESS_DROP_THRESHOLD:
                print("Detected loudness drop")
                res.append(section)
            prev = section['loudness']
        
        return res

    def update_playback_state(self):
        playback_state = self.sp.current_playback()
        self.device_id = playback_state['device']['id']
        self.device_is_active = playback_state['device']['is_active']
        self.playback_progress_sec = round(playback_state['progress_ms']/1000, 2)
        self.is_playing =  playback_state['is_playing']
        self.current_id = playback_state['item']['id']

    # monitors for when to skip songs
    def monitor_playback(self):

        while True:
            self.update_playback_state()

            if self.is_playing:
                try:
                    result = self.sp.audio_analysis(self.current_id)
                except Exception as e:
                    print("An error occured", e)
                target_sections = self.get_loudness_drop_sections(result['sections'])
                print(target_sections)
                if target_sections:
                    self.update_playback_state()
                    target_time = target_sections[0]['start']
                    print("target skip time", target_time)
                    sleep_time = target_time - self.playback_progress_sec 
                    print("sleeping", sleep_time)

                    sleep(sleep_time)
                    # self.update_playback_state()

                    # if abs(self.playback_progress_sec - target_time) < 0.5:
                    self.sp.next_track()
            
    
# CLIENT_ID="04b4169e7d6b48df9d7d68fafbe54b1d"
# CLIENT_SECRET="93180012ca944d9da595cd952ff67bb6"
# REDIRECT_URI="http://localhost:3000/callback"
# spotify = SpotifyAPI(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
# spotify.auth()
# print(spotify.get_user_devices())
# spotify.load_cadence_data([])
# spotify.get_top_songs_data()
# spotify.add_to_song_list()
# spotify.add_songs_to_queue()
# spotify.create_playlist()