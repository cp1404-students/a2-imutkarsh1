
import csv
# Constants
UNLEARNED = 'u'
LEARNED = 'l'
CSV_FILE = 'songs.csv'


def main():
    """Main function to run the program."""
    print("Song List 1.0 - by [UTKARSH PATHAK]")
    songs = load_songs()
    print(f"{len(songs)} songs loaded.")

    while True:
        choice = display_menu()
        if choice == 'D':
            display_songs(songs)
        elif choice == 'A':
            add_song(songs)
        elif choice == 'C':
            complete_song(songs)
        elif choice == 'Q':
            save_songs(songs)
            print(f"{len(songs)} songs saved to {CSV_FILE}")
            print("Make some music!")
            break


def load_songs():
    """Load songs from the CSV file."""
    songs = []
    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                songs.append(row)
    except FileNotFoundError:
        print(f"Warning: {CSV_FILE} not found. Starting with an empty song list.")
    return songs


def save_songs(songs):
    """Save songs to the CSV file."""
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for song in songs:
            writer.writerow(song)


def display_menu():
    """Display the user menu and get the user's choice."""
    print("\nMenu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")
    choice = input(">>> ").upper()
    while choice not in ['D', 'A', 'C', 'Q']:
        print("Invalid menu choice")
        choice = input(">>> ").upper()
    return choice


def display_songs(songs):
    """Display the list of songs."""
    songs_sorted = sorted(songs, key=lambda x: (x[1].lower(), x[0].lower()))
    learned_count = sum(1 for song in songs_sorted if song[3] == LEARNED)
    unlearned_count = len(songs_sorted) - learned_count

    for i, song in enumerate(songs_sorted, start=1):
        learned_marker = ' ' if song[3] == LEARNED else '*'
        print(f"{i}. {learned_marker} {song[0]} - {song[1]} ({song[2]})")
    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")


def add_song(songs):
    """Add a new song to the list."""
    print("Enter details for a new song.")
    title = get_nonempty_input("Title: ")
    artist = get_nonempty_input("Artist: ")
    year = get_positive_int("Year: ")
    songs.append([title, artist, str(year), UNLEARNED])
    print(f"{title} by {artist} ({year}) added to song list.")


def complete_song(songs):
    """Mark a song as learned."""
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    print("Enter the number of a song to mark as learned.")
    song_num = get_int_in_range(1, len(unlearned_songs), ">>> ")
    song_to_learn = unlearned_songs[song_num - 1]
    song_to_learn[3] = LEARNED
    print(f"{song_to_learn[0]} by {song_to_learn[1]} learned")


def get_nonempty_input(prompt):
    """Get non-empty input from the user."""
    user_input = input(prompt).strip()
    while not user_input:
        print("Input can not be blank.")
        user_input = input(prompt).strip()
    return user_input


def get_positive_int(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_int_in_range(min_value, max_value, prompt):
    """Get an integer from the user within a specified range."""
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Number must be between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input; enter a valid number.")


if __name__ == "__main__":
    main()

