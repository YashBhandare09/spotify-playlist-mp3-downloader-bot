import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp

# Constants
SPOTIFY_CLIENT_ID = 'b33d10758c604e7e91080140161787b0'
SPOTIFY_CLIENT_SECRET = '9c55bf806c344d53b88c6dfea82a3045'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'
DOWNLOAD_DIR = './downloads'

# Initialize Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-read-private playlist-read-collaborative"
))

def sanitize_filename(filename):
    """Remove invalid characters from filenames."""
    return re.sub(r'[\/:"*?<>|]', '', filename)

def fetch_playlist_tracks(playlist_id):
    """Fetch all tracks from a Spotify playlist (with pagination)."""
    print("Fetching playlist tracks...")
    tracks = []
    results = sp.playlist_items(playlist_id, fields="items(track(name,artists(name))),next")

    while results:
        for item in results.get('items', []):
            track = item.get('track')
            if isinstance(track, dict) and 'name' in track and track.get('artists'):
                title = track['name']
                artist = track['artists'][0]['name']
                tracks.append({"title": title, "artist": artist})

        results = sp.next(results) if results and results.get("next") else None

    return tracks

def search_youtube(song_title, artist):
    """Search YouTube for a song and return the first result."""
    query = sanitize_filename(f"{song_title} {artist}")
    ydl_opts = {'quiet': True, 'default_search': 'ytsearch1'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(query, download=False)
            if 'entries' in result and result['entries']:
                return result['entries'][0]['webpage_url']
        except yt_dlp.utils.DownloadError as e:
            print(f"Error searching YouTube for {song_title} by {artist}: {e}")

    return None

def download_audio(url, output_path):
    """Download audio from YouTube directly as MP3."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded and converted to MP3: {output_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    playlist_id = "https://open.spotify.com/playlist/7e5uvvPoGwXIwh8t9bTwNq?si=24cf1221cf7d4942&pt=c9bc184b410ddfd175daff0ab2542ffa"

    # Ensure the download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Fetch playlist tracks
    tracks = fetch_playlist_tracks(playlist_id)

    # Process each track
    for track in tracks:
        title = track['title']
        artist = track['artist']
        output_file = os.path.join(DOWNLOAD_DIR, f"{sanitize_filename(title)} - {sanitize_filename(artist)}.mp3")

        if os.path.exists(output_file):
            print(f"File already exists: {output_file}")
            continue

        print(f"Processing: {title} by {artist}")
        youtube_url = search_youtube(title, artist)

        if youtube_url:
            download_audio(youtube_url, output_file)
        else:
            print(f"Could not find YouTube link for: {title} by {artist}")

    print("All tracks processed!")

if __name__ == "__main__":
    main()
