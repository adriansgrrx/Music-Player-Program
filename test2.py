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
        self.song_queue = collections.deque()
        self.library = []
        self.history = collections.deque()

    def add_to_library(self, song):
        self.library.append(song)

    def search_song(self, title):
        for song in self.library:
            if song.title == title:
                return song
        return None

    def sort_library(self, key=lambda x: x.title):
        self.library.sort(key=key)

    def play_next_song(self):
        if not self.song_queue:
            print("No songs in the queue.")
        else:
            song = self.song_queue.popleft()
            self.history.append(song)
            print(f"Playing {song}")

    def play_previous_song(self):
        if not self.history:
            print("No previous songs in history.")
        else:
            song = self.history.pop()
            self.song_queue.appendleft(song)
            print(f"Playing previous song: {song}")

# Default storage of songs
default_songs = [
    Song("Hello", "Adele", 320),
    Song("Shape of You", "Ed Sheeran", 250),
    Song("Despacito", "Luis Fonsi", 290),
    Song("Sugar", "Maroon 5", 200),
    Song("Thriller", "Michael Jackson", 360),
]

player = MusicPlayer()

# Add default songs to the library
for song in default_songs:
    player.add_to_library(song)

# Access all the songs in the library
print("All the songs in the library:")
for song in player.library:
    print(song)
