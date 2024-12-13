import os
import time
import yt_dlp
import vlc

# Define playlist with default name
playlist = []

# Function to play the song
def play_song(song_name):
    print(f"Playing: {song_name}")
    # Use yt_dlp to fetch the song URL
    ydl_opts = {
        'quiet': True,  # Silence output from yt_dlp
        'format': 'bestaudio/best',  # Get best audio quality
        'outtmpl': 'response.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        video_url = info_dict['entries'][0]['url']

    # Initialize VLC media player
    player = vlc.MediaPlayer()
    media = vlc.Media(video_url)
    player.set_media(media)
    player.play()

    # Control flow while song is playing
    paused = False
    while True:
        print("\nOptions while song is playing:")
        print("Press 'd' to download (audio/video).")
        print("Press 'p' to add to playlist.")
        print("Press 'r' to remove from playlist.")
        print("Enter a number to seek (in seconds).")
        print("Press 'k' to pause/resume.")
        print("Press 'q' to stop the song and return to the main menu.")

        choice = input("Enter your choice: ")

        if choice == 'd':
            download_option = input("Do you want to download audio or video? (audio/video): ").strip().lower()
            if download_option == 'audio':
                download_song(song_name, download_audio=True, download_video=False)
            elif download_option == 'video':
                download_song(song_name, download_audio=False, download_video=True)
            else:
                print("Invalid option. Please choose 'audio' or 'video'.")
        elif choice == 'p':
            playlist.append(song_name)
            print(f"{song_name} added to playlist.")
        elif choice == 'r':
            if song_name in playlist:
                playlist.remove(song_name)
                print(f"{song_name} removed from playlist.")
            else:
                print(f"{song_name} is not in the playlist.")
        elif choice == 'k':
            if paused:
                player.play()
                print("Resumed playing.")
                paused = False
            else:
                player.pause()
                print("Paused.")
                paused = True
        elif choice.isdigit():
            seek_seconds = int(choice)
            player.set_time(seek_seconds * 1000)  # VLC expects milliseconds
            print(f"Seeked to {seek_seconds} seconds.")
        elif choice == 'q':
            print("Stopping the song and going back to the main menu.")
            player.stop()
            break
        else:
            print("Invalid choice. Please try again.")

# Function to download the song
def download_song(song_name, download_audio=False, download_video=False):
    ydl_opts = {
        'quiet': True,
        'format': 'bestaudio/best' if download_audio else 'best',
        'outtmpl': 'response.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=True)
        print(f"Downloaded {song_name}.")
    if download_audio:
        os.rename('response.mp3', f'{song_name}.mp3')
        print(f"Audio downloaded as {song_name}.mp3")
    if download_video:
        os.rename('response.mp4', f'{song_name}.mp4')
        print(f"Video downloaded as {song_name}.mp4")

# Function to play the playlist
def play_playlist():
    if not playlist:
        print("The playlist is empty!")
        return
    print("Playing playlist...")
    paused = False
    for song in playlist:
        print(f"Now playing: {song}")
        # Use yt_dlp to fetch the song URL
        ydl_opts = {
            'quiet': True,
            'format': 'bestaudio/best',  # Get best audio quality
            'outtmpl': 'response.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{song}", download=False)
            video_url = info_dict['entries'][0]['url']

        # Initialize VLC media player
        player = vlc.MediaPlayer()
        media = vlc.Media(video_url)
        player.set_media(media)
        player.play()

        while True:
            print("\nOptions while song is playing:")
            print("Press 'k' to pause/resume.")
            print("Press 'n' to skip to the next song.")
            print("Press 'e' to exit the playlist and return to the main menu.")

            choice = input("Enter your choice: ")

            if choice == 'k':
                if paused:
                    player.play()
                    print("Resumed playing.")
                    paused = False
                else:
                    player.pause()
                    print("Paused.")
                    paused = True
            elif choice == 'n':
                print("Skipping to the next song.")
                player.stop()
                break
            elif choice == 'e':
                print("Exiting playlist.")
                player.stop()
                return
            else:
                print("Invalid choice. Please try again.")
        player.stop()

# Main function to handle user choices
def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Play a song")
        print("2. Play Playlist")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            song_name = input("Please type the song name you want to hear: ")
            play_song(song_name)
        elif choice == '2':
            play_playlist()
        elif choice == '3':
            print("GOOD BYE, HAVE A NICE DAY.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == '__main__':
    main()

