# A song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
# Return a string with just the words of the song.

def song_decoder(song):
    song = song.replace("WUB", " ")
    while '  ' in song:
        song = song.replace("  ", " ")
    if song[0] == " ":
        song = song[1:]
    if song[-1] == " ":
        song = song[:-1]
    print(song)
    return song

# More succinctly:
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())
