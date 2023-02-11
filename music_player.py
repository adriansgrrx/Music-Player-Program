import collections
import time

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f"{self.title} by {self.artist}, {self.duration} seconds"

class MusicPlayer:
    def __init__(self):
        self.songQueue = collections.deque()
        self.playlist = []
        self.history = collections.deque()

    def durationCountdown(self, duration):
        while duration:
            mins, secs = divmod(duration, 60)
            timeFormat = '{:02d}:{:02d}'.format(mins, secs)
            print(f"                                        {timeFormat}", end='\r')
            time.sleep(1)
            duration -= 1

    def addToPlaylist(self, song):
        self.playlist.append(song)

    def searchSong(self, title):
        for song in self.playlist:
            if song.title == title:
                print(f"                        Now playing: {song.title} by {song.artist}")
                self.history.append(song)
                return song
        return print("                        The song is not on your playlist.")

    def playAllSongs(self):
        for song in player.playlist:
            print(f"                        Now playing, {song.title} by {song.artist}")
            player.durationCountdown(song.duration)

    def playNextSong(self):
        if not self.songQueue:
            print("                        No songs in the queue.")
        else:
            song = self.songQueue.popleft()
            self.history.append(song)
            print(f"                        Next song playing: {song.title} by {song.artist}")
            
    def playPrevSong(self):
        if not self.history:
            print("                        No previous songs in the playlist.")
        else:
            song = self.history.pop()
            self.songQueue.appendleft(song)
            print(f"                        Previous song playing: {song.title} by {song.artist}")

player = MusicPlayer()

# By default, these are the songs to play.
yourSongs = [
    Song("Flowers", "Miley Cyrus", 200),
    Song("Kill Bill", "Sza", 154),
    Song("Creepin'", "The Weeknd", 222),
    Song("As it Was", "Harry Styles", 167),
    Song("Unholy", "Sam Smith", 157),
    Song("golden hour", "JVKE",  209),
    Song("Anti-Hero", "Taylor Swift",  201),
    Song("Here With Me", "d4vid",  242),
    Song("Made You Look", "Megan Trainor",  134),
    Song("Lavander Haze", "Taylor Swift",  202),
]

# Add every songs to the playlist and to the queue
for song in yourSongs:
    player.addToPlaylist(song)
    player.songQueue.append(song)

# player.searchSong("Lavander Haze")
# player.playNextSong()
# player.playPrevSong()

# This is for aesthetic purposes only, a function to center a text output.
textsToBeCentered = []
def centerOutput(text):
    width = 80
    left_padding = (width - len(text))//2
    right_padding = width - len(text) - left_padding
    print(" " * left_padding + text + " " * right_padding)

def welcomeUser():
    welcomeLine = "Welcome to SoundScape!"
    tagline = "Your sound track to life.\n\n"
    yourSongsText = "Your Songs:"
    textsToBeCentered.append(welcomeLine)
    textsToBeCentered.append(tagline)
    textsToBeCentered.append(yourSongsText)

    for song in player.playlist:
        songTitles = f"{song.title} by {song.artist}"
        textsToBeCentered.append(songTitles)

def main():
    welcomeUser()
    for text in textsToBeCentered:
        centerOutput(text)
    commands = int(input("\nHere are the commands:\n1. Play all\n2. Play a song\n3. Search a song\n>>> "))
    if commands == 1:
        player.playAllSongs()


main()
    

