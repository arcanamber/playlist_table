# !/usr/bin/python3
# Amber Jennings 2023

print("Playlist Storage Program\n")
start = int(input("1. Start Program\n2. Quit\n>> "))

def store_song(count, playlist):
    output = "\n".join(["|".join(song.values()) for song in playlist])
    file.write(f"{output}\n")

if start == 1:
    amount = int(input("\nHow many songs would you like to enter?\n>> "))
    count = 0
    playlist = []

    while count < amount:
        print(f"Song #{count + 1}")
        title = input("Song title: ")
        artists = input("Artist(s): ")
        album = input("Album name: ")
        length = input("Song length: ")
        print()

        song = {
            "Title: "       : title,
            "Artist(s): "   : artists,
            "Album: "       : album,
            "Song length: " : length
        }

        playlist.append(song)
        count += 1

    output = ""
    with open("playlist.md", "a+") as file:
        file.seek(0)
        content = file.read()

        if len(content) == 0:
            file.write("|Title|Artist(s)|Album|Length|\n|---|---|---|---|\n")
            store_song(count, playlist)
            print("Playlist stored - see \"playlist.md\"\n")

        else:
            if "|Title|Artist(s)|" in content:
                store_song(count, playlist)
                print("Playlist updated - see \"playlist.md\"\n")

            else:
                print("It looks like \"playlist.md\" already contains other information. Please move or delete it and try again.")
                
    print("Goodbye!")

else:
    print("Goodbye!")
