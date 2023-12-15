import json

class SongCollection:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        """Add a single Song object to the song list."""
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Get the number of unlearned songs."""
        return sum(1 for song in self.songs if song.status == 'u')

    def get_number_of_learned_songs(self):
        """Get the number of learned songs."""
        return sum(1 for song in self.songs if song.status == 'l')

    def load_songs_from_json(self, json_file):
        """Load songs from JSON file into the list of Song objects."""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.songs = [Song(song['title'], song['artist'], song['year'], song['status']) for song in data]
        except FileNotFoundError:
            print(f"Warning: {json_file} not found. Starting with an empty song list.")

    def save_songs_to_json(self, json_file):
        """Save songs from the song list into JSON file."""
        data = [{'title': song.title, 'artist': song.artist, 'year': song.year, 'status': song.status} for song in self.songs]
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

    def sort_songs(self, key):
        """Sort songs by the key passed in, then by title."""
        self.songs.sort(key=lambda x: (getattr(x, key), x.title.lower()))

