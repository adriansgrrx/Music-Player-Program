import collections

playlist = {
    "Flowers": {
        "title": "Flowers",
        "artist": "Miley Cyrus", 
        "duration": 200 
    },

    "Kill Bill": {
        "title": "Kill Bill",
        "artist": "Sza", 
        "duration": 154 
    },

    "Creepin'": {
        "title": "Creepin'",
        "artist": "The Weeknd & 21 Savage", 
        "duration": 217
    },
}

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

    def add_to_library(self, song):
        self.library.append(song)

    def play_next_song(self):
        if not self.song_queue:
            print("No songs in the queue.")
        else:
            song = self.song_queue.popleft()
            print(f"Playing {song}")

player = MusicPlayer()

# Add some songs to the library
player.add_to_library(Song(playlist["Flowers"]["title"], playlist["Flowers"]["artist"], playlist["Flowers"]["duration"]))
player.add_to_library(Song(playlist["Kill Bill"]["title"], playlist["Kill Bill"]["artist"], playlist["Kill Bill"]["duration"]))
player.add_to_library(Song(playlist["Creepin'"]["title"], playlist["Creepin'"]["artist"], playlist["Creepin'"]["duration"]))

# Add songs to the queue
player.song_queue.append(player.library[0])
player.song_queue.append(player.library[1])
player.song_queue.append(player.library[2])

# Play the next song in the queue
player.play_next_song()
player.play_next_song()
player.play_next_song()
print(player.library)
print(player.library[1])
print(player.library[2])