import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify app credentials
SPOTIPY_CLIENT_ID = '6504211e563740abbbb260a35a658c11'
SPOTIPY_CLIENT_SECRET = '63d04163ca944969962a64286745db90'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

scope = "playlist-read-private playlist-modify-private playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

user_id = sp.current_user()['id']

# Source playlist (contains your 2025 songs)
source_playlist_id = 'your_source_playlist_id'

# New playlist name
new_playlist_name = '2025 Songs'

# Create new playlist if not exists
new_playlist = sp.user_playlist_create(user=user_id, name=new_playlist_name, public=False)

# Get all tracks from source playlist
results = sp.playlist_items(source_playlist_id)
tracks_2025 = []

for item in results['items']:
    track = item['track']
    release_year = int(track['album']['release_date'].split('-')[0])
    if release_year == 2025:
        tracks_2025.append(track['uri'])

# Add tracks to new playlist
if tracks_2025:
    sp.playlist_add_items(new_playlist['id'], tracks_2025)

print(f"Added {len(tracks_2025)} tracks to '{new_playlist_name}'!")
