# Python-Music-Player
 It allows users to search for songs, play them directly, create and manage playlists, and even download audio or video files.


 Features:
Search and Play Songs

Users can search for songs by typing the song name.
The script uses yt-dlp to fetch the best available audio or video streams.
Playback is handled using the vlc media player library.
Interactive Controls During Playback

Pause/Resume the song.
Seek to a specific timestamp.
Add the current song to a playlist.
Remove the song from the playlist.
Download the song (audio or video).
Stop the playback and return to the main menu.
Playlist Management

Users can add songs to a playlist.
Play the entire playlist sequentially.
Skip songs or exit the playlist playback.
Download Functionality

Allows users to download songs in either audio or video format.
Saves the downloaded files with the song name for easy access.
Main Menu

Provides a simple and intuitive menu with options to:
Play a song.
Play the playlist.
Exit the program.
How It Works:
Play a Song

Enter the name of the song in the search prompt.
The script searches YouTube and streams the best audio/video URL.
Users can interact with the playback using the provided controls.
Download Songs

During playback, users can opt to download either the audio or video version of the song.
Manage and Play Playlist

Songs can be added or removed from the playlist during playback.
Playlists can be played sequentially with options to pause, skip, or exit.
Exit

Gracefully exits the program after thanking the user.
Modules Used:
yt_dlp: For fetching YouTube URLs and downloading songs.
vlc: For media playback.
os: For handling file operations.
time: For delays and time-based operations.
Pre-requisites:
Install Required Libraries:

Install yt-dlp using:
pip install yt-dlp

Install python-vlc using:
pip install python-vlc

Ensure You Have Internet Access:
The script fetches songs from YouTube, requiring an active internet connection.

Run the script:
python music_player.py


Follow the main menu options:

Type 1 to search and play a song.
Type 2 to play your saved playlist.
Type 3 to exit the program.
During playback, use the interactive options to control the song.

Download songs as audio or video by choosing the d option during playback.

Manage playlists by adding or removing songs, and enjoy seamless playback.

This script provides a complete and interactive experience for music enthusiasts, leveraging the power of YouTube and VLC for high-quality streaming and playback.










