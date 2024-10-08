from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    album_choice = int(input())
    if 1 <= album_choice <= len(albums):
        songs_list = albums[album_choice - 1][SONGS_LIST_INDEX]
    else:
        print("Exiting")
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(albums):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Now Playing: {}".format(title))
        print("*" * 30)
    else:
        print("Invalid choice start again")
        continue
