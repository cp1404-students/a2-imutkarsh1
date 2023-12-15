class Song:
    def __init__(self, title, artist, year, status='u'):
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year}) - Status: {self.status}"

    def mark_as_learned(self):
        """Mark the song as learned."""
        self.status = 'l'

    def mark_as_unlearned(self):
        """Mark the song as unlearned."""
        self.status = 'u'


