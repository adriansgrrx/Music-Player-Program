import collections
import time
import msvcrt

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

    def addToPlaylist(self, song):
        self.playlist.append(song)
        self.sortPlaylist()

    def durationCountdown(self, duration):
        while duration:
            duration -= 1
            mins, secs = divmod(duration, 60)
            timeFormat = '{:02d}:{:02d}'.format(mins, secs)
            print(f"                                    {timeFormat}", end='\r')
            time.sleep(1)
            if msvcrt.kbhit():
                key = msvcrt.getch().decode("utf-8")
                if key == "N":
                    self.playNextSong()
                if key == "P":
                    self.playPrevSong()
                if key == "X":
                    print("\n                           Music player stopped.\n")
                    commands()

    def playAllSongs(self):
        for song in self.playlist:
            self.songQueue.popleft()
            self.songQueue.append(song)
            self.history.appendleft(song)
            print(f"\n                      Now playing: {song.title} by {song.artist}")
            self.durationCountdown(song.duration)

    def playSingleSong(self, title):
        for song in self.playlist:
            lowerSong = song.title.lower()
            if  lowerSong == title:
                displayOnPlayCommands()
                print(f"\n                       Now playing: {song.title} by {song.artist}")
                self.durationCountdown(song.duration)
                print(f"                            The music is done playing.\n")
                break
        else:
            print("\n                         Song not found in the playlist.")
            commands()

    def searchSong(self, title):
        for song in self.playlist:
            lowerSong = song.title.lower()
            if  lowerSong == title:
                displayOnPlayCommands()
                print(f"\n                      Search Result: {song.title.title()} by {song.artist.title()}")
                try:
                    permission = input(f"                     Do you want to play {song.title.title()}? [y/n]\n                                 >>> ").lower()
                    if permission == "y":
                        self.songQueue.popleft()
                        self.history.appendleft(song)
                        print(f"\n                      Now playing: {song.title} by {song.artist}")
                        self.durationCountdown(song.duration)
                    elif permission == "n":
                        commands()
                except ValueError:
                    print("[INVALID INPUT]")
                break
        else:
            print("\n                         Song not found in the playlist.")
            commands()

    def playPrevSong(self):
        if not self.history:
            print("\n                         No previous songs in the playlist.\n")
            commands()
        else:
            getSong = self.history.popleft()
            self.songQueue.append(getSong)
            print(f"\n                      Previous Song playing: {getSong.title} by {getSong.artist}")
            self.durationCountdown(getSong.duration)

    def playNextSong(self):
        if not self.songQueue:
            print("\n                           No songs in the queue.\n")
            commands()
        else:
            song = self.songQueue.popleft()
            self.history.appendleft(song)
            print(f"\n                      Next song playing: {song.title} by {song.artist}")
            self.durationCountdown(song.duration)

    def addSong(self, title, artist, duration):
        newSong = Song(title, artist, duration)
        self.addToPlaylist(newSong)
        # yourSongs.append(newSong)
        
        self.sortPlaylist()
        print()
        yourSongsText = "Updated Version of Your Songs:"
        textsToBeCentered.append(yourSongsText)

        for song in self.sortedPlaylist:
            songTitles = f"{song.title.title()} by {song.artist.title()}"
            textsToBeCentered.append(songTitles)
        for text in textsToBeCentered:
            centerOutput(text)
        textsToBeCentered.clear()
        commands()

    def deleteSong(self, title):
        for i, song in enumerate(self.playlist):
            if song.title.lower() == title:
                self.playlist.pop(i)
                
                print()
                yourSongsText = "Updated Version of Your Songs:"
                textsToBeCentered.append(yourSongsText)

                self.sortPlaylist()
                for song in self.sortedPlaylist:
                    songTitles = f"{song.title.title()} by {song.artist.title()}"
                    textsToBeCentered.append(songTitles)
                for text in textsToBeCentered:
                    centerOutput(text)
                textsToBeCentered.clear()
                print(f"\n                  '{title.title()}' has been deleted from the playlist.")

                commands()
        print(f"                    Song with title '{title.title()}' not found.")


    def sortPlaylist(self, key=lambda song: song.title[0].lower()):
        self.playlist.sort(key=key)
        self.sortedPlaylist = self.playlist
        self.songQueue = collections.deque(self.sortedPlaylist)

player = MusicPlayer()

# By default, these are the UNSORTED songs available to play.
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

# Add every song to the playlist and to the queue
for song in yourSongs:
    player.addToPlaylist(song)
    player.songQueue.append(song)

# This is for aesthetic purposes only. A function to center a text output.
# ************************************************************************
textsToBeCentered = []
txtDisplayOnPlayCommands = []
def centerOutput(text):
    width = 80
    left_padding = (width - len(text))//2
    right_padding = width - len(text) - left_padding
    print(" " * left_padding + text + " " * right_padding)

def displayOnPlayCommands():
    print()
    onPlayCommand1 = "Press [N] to play the next song"
    onPlayCommand2 = "Press [P] to play the previous song"
    onPlayCommand3 = "Press [X] to stop the song"
    txtDisplayOnPlayCommands.append(onPlayCommand1)
    txtDisplayOnPlayCommands.append(onPlayCommand2)
    txtDisplayOnPlayCommands.append(onPlayCommand3)
    for text in txtDisplayOnPlayCommands:
        centerOutput(text)
    txtDisplayOnPlayCommands.clear()

def welcomeUser():
    welcomeLine = "Welcome to SoundScape!"
    tagline = "Your sound track to life.\n\n"
    yourSongsText = "Your Songs:"
    textsToBeCentered.append(welcomeLine)
    textsToBeCentered.append(tagline)
    textsToBeCentered.append(yourSongsText)

    player.sortPlaylist()
    for song in player.sortedPlaylist:
        songTitles = f"{song.title} by {song.artist}"
        textsToBeCentered.append(songTitles)
    for text in textsToBeCentered:
        centerOutput(text)
    textsToBeCentered.clear()
# ************************************************************************
def commands():
    while True:
        try:
            commands = int(input("\nHere are the commands:\n1. Play all\n2. Play a song\n3. Search a song\n4. Add a song\n5. Delete a song\n>>> "))
            if commands == 1:
                displayOnPlayCommands()
                player.playAllSongs()

            elif commands == 2:
                try:
                    selectedSong = str(input("\n                               Song title: "))
                    player.playSingleSong(selectedSong.lower())
                except ValueError:
                    print("[Invalid Input]")

            elif commands == 3:
                while True:
                    try:
                        selectedSong = str(input("\n                           Song title: "))
                        player.searchSong(selectedSong.lower())
                    except ValueError:
                        print("[Invalid Input]")

            elif commands == 4:
                try:
                    songTitle = str(input("\n                           Song title: ")).lower()
                    songArtist = str(input("                           Artist: ")).lower()
                    songDuration = int(input("                           Duration (sec): "))
                    player.addSong(songTitle, songArtist, songDuration)
                except ValueError:
                    print("\n                           Enter proper format for duration.")

            elif commands == 5:
                # try:
                    delSong = str(input("\n                           Song title: ")).lower()
                    player.deleteSong(delSong)
                # except ValueError:
                #     print("\n                           Enter proper format for duration.")

        except ValueError:
            print("[Invalid Input]")

def main():
    welcomeUser()
    commands()

main()