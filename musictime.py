class Song:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.duration} ({self.genre})"


class Album:
    def __init__(self, title, artist, release_year):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.release_year})"


class MusicLibrary:
    def __init__(self):
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def display_albums(self):
        for album in self.albums:
            print(album)
            for song in album.songs:
                print(f"\t- {song}")

# Example usage:

# Create songs
song1 = Song("Song 1", "3:45", "Pop")
song2 = Song("Song 2", "4:20", "Rock")
song3 = Song("Song 3", "3:30", "Jazz")

# Create albums and add songs
album1 = Album("Album 1", "Artist 1", 2022)
album1.add_song(song1)
album1.add_song(song2)

album2 = Album("Album 2", "Artist 2", 2023)
album2.add_song(song3)

# Create a music library and add albums
library = MusicLibrary()
library.add_album(album1)
library.add_album(album2)

# Display albums and songs
library.display_albums()