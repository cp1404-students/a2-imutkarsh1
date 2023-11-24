from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from song import Song
from songcollection import SongCollection


class SongListApp(App):
    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs_from_json('songs.json')
        return self.create_layout()

    def create_layout(self):
        main_layout = BoxLayout(orientation='horizontal')

        # Left side layout for adding new songs
        left_layout = self.create_left_layout()

        # Right side layout for displaying songs
        right_layout = self.create_right_layout()

        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_layout)

        return main_layout

    def create_left_layout(self):
        left_layout = BoxLayout(orientation='vertical', size_hint_x=0.25)
        # Add your widgets to the left layout
        # ...

        # Return the left layout
        return left_layout

    def create_right_layout(self):
        self.right_layout = BoxLayout(orientation='vertical', size_hint_x=0.75)
        self.update_song_list()
        # Return the right layout
        return self.right_layout

    def update_song_list(self):
        # Clear the current list of buttons
        self.right_layout.clear_widgets()

        # Create a scroll view for song buttons
        scroll_view = ScrollView()
        song_list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        song_list_layout.bind(minimum_height=song_list_layout.setter('height'))

        for song in self.song_collection.songs:
            btn = Button(text=str(song), size_hint_y=None, height=40)
            btn.bind(on_release=self.toggle_song_status)
            song_list_layout.add_widget(btn)

        scroll_view.add_widget(song_list_layout)
        self.right_layout.add_widget(scroll_view)

    def toggle_song_status(self, instance):
        # Logic to toggle song status
        song_details = instance.text.split(' by ')[0].strip()  # Simplistic parsing, you may need something more robust
        for song in self:songcollection
