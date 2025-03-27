import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

def filter_playlist(sp, source_playlist_id):
    """
    Filter songs from a source playlist:
    - Remove explicit songs
    - Only include songs added in the past 2 years
    
    :param sp: Spotipy client
    :param source_playlist_id: ID of the source playlist
    :return: List of track URIs that match the criteria
    """
    # Calculate the date 2 years ago
    two_years_ago = datetime.now() - timedelta(days=365 * 2)
    
    # Retrieve all tracks from the source playlist
    results = sp.playlist_tracks(source_playlist_id)
    tracks = results['items']
    
    # Fetch additional tracks if the playlist is large
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    # Filter tracks based on criteria
    filtered_tracks = []
    for item in tracks:
        track = item['track']
        
        # Check if the track was added in the past 2 years
        added_at = datetime.strptime(item['added_at'], "%Y-%m-%dT%H:%M:%SZ")
        
        # Filter conditions
        if (not track['explicit'] and  # Not an explicit track
            added_at > two_years_ago):  # Added within the past 2 years
            filtered_tracks.append(track['uri'])
    
    return filtered_tracks

def create_filtered_playlist(sp, user_id, playlist_name, filtered_tracks):
    """
    Create a new playlist with filtered tracks, adding in batches.
    
    :param sp: Spotipy client
    :param user_id: Spotify user ID
    :param playlist_name: Name of the new playlist
    :param filtered_tracks: List of track URIs to add
    :return: ID of the newly created playlist
    """
    # Create a new playlist
    new_playlist = sp.user_playlist_create(
        user=user_id, 
        name=playlist_name, 
        public=False  # Make it a private playlist
    )
    
    # Add tracks in batches of 100
    batch_size = 100
    for i in range(0, len(filtered_tracks), batch_size):
        batch = filtered_tracks[i:i+batch_size]
        sp.playlist_add_items(new_playlist['id'], batch)
    
    return new_playlist['id']

def main():
    # Set up Spotify authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='Client id',
        client_secret='client secret',
        redirect_uri='http://localhost:8888/callback',
        scope='playlist-modify-public playlist-modify-private playlist-read-private'
    ))
    
    # Get the current user's ID
    user_id = sp.me()['id']
    
    # Playlist ID from the Spotify URL
    source_playlist_id = 'source playlist id'
    
    # Filter the tracks
    filtered_tracks = filter_playlist(sp, source_playlist_id)
    
    # Create a new playlist with filtered tracks
    new_playlist_id = create_filtered_playlist(
        sp, 
        user_id, 
        'Non-Explicit Tracks (Past 2 Years)', 
        filtered_tracks
    )
    
    print(f"New playlist created with {len(filtered_tracks)} tracks")
    print(f"Playlist ID: {new_playlist_id}")

if __name__ == '__main__':
    main()