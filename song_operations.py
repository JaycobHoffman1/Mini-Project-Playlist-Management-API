from playlists import playlists

def find_song(target_song):
    for playlist in playlists.keys():
        # Linear search algorithm
        for song in playlists[playlist]:
            if song == target_song:
                return (True, playlist)
    return (False,)

# POST

def add_song(playlist, song):
    if playlists.get(playlist, False):
        playlists[playlist].append(song)
        return
    playlists[playlist] = []
    playlists[playlist].append(song)

# GET

def read_song(target_song):
    song_exists = find_song(target_song)
    if song_exists[0]:
        playlist = song_exists[1]
        return f'"{target_song}" found in "{playlist}" playlist.'
    return False

# PUT

def edit_song(original_song, updated_song):
    song_exists = find_song(original_song)
    if song_exists[0]:
        playlist = song_exists[1]
        playlists[playlist][playlists[playlist].index(original_song)] = updated_song
        return True
    return False

# DELETE

def remove_song(target_song):
    song_exists = find_song(target_song)
    if song_exists[0]:
        playlist = song_exists[1]
        playlists[playlist].remove(target_song)
        return True
    return False
