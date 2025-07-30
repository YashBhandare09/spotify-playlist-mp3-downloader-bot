# 🎵 Spotify Playlist Songs Downloader Bot

This Python bot fetches all songs from any public or private Spotify playlist using the Spotify API, searches for them on YouTube, and downloads them as MP3 files using `yt-dlp`.

> ⚠️ This project is for educational purposes only. Please ensure you follow copyright laws and Spotify's & YouTube's terms of service.

## 📌 Features

- ✅ Fetch songs from Spotify playlists
- ✅ Search corresponding YouTube videos automatically
- ✅ Download and convert audio to `.mp3` using `yt-dlp`
- ✅ Automatically skip already-downloaded files

## 🛠️ Requirements

- Python 3.7 or later
- A Spotify Developer account
- `yt-dlp`
- `ffmpeg` (for audio conversion)
- Python packages:
  - `spotipy`
  - `yt-dlp`

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/spotify-playlist-mp3-downloader-bot.git
cd spotify-playlist-mp3-downloader-bot
```

### 2. Install dependencies
```bash
pip install spotipy yt-dlp
```

### 3. Install FFmpeg
Make sure `ffmpeg` is installed and added to your system's PATH.

- [Download FFmpeg](https://ffmpeg.org/download.html)

### 4. Set up your Spotify Developer credentials
Create an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

Replace credentials in `main.py`.

## ▶️ How to Use

1. Replace your Spotify playlist URL in `main()` function.
2. Run the script using:
```bash
python main.py
```
3. MP3 files will be saved in `./downloads`

## 📂 Project Structure

```
spotify-playlist-mp3-downloader-bot/
├── downloads/
├── main.py
├── README.md
└── .gitignore
```

## 📄 Disclaimer

This tool is provided for educational purposes only. Downloading copyrighted material may violate Spotify or YouTube’s terms.

## 🙌 Acknowledgments

- [Spotipy](https://spotipy.readthedocs.io/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
