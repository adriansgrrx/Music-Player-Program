import collections

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

    def addToPlaylist(self, song):
        self.playlist.append(song)

    def playNextSong(self):
        if not self.songQueue:
            print("No songs in the queue.")
        else:
            song = self.songQueue.popleft()
            print(f"Playing {song}")

player = MusicPlayer()

# Add some songs to the playlist
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

# Add songs to the queue
for song in yourSongs:
    player.addToPlaylist(song)
print(song)

# Play the next song in the queue
print(player.playlist)
# print(player.playlist[1])
# print(player.playlist[2])