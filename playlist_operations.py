from playlists import playlists

def find_playlist(target_playlist):
    for playlist in playlists.keys():
        if playlist == target_playlist:
            return (True, playlist)
    return (False,)

# GET

def read_playlist(target_playlist):
    playlist_exists = find_playlist(target_playlist)
    if playlist_exists[0]:
        playlist = playlist_exists[1]
        return f'Playlist "{playlist}" contains the following playlists: {playlists[playlist]}.'
    return False

# PUT

def edit_playlist(original_playlist, updated_playlist):
    playlist_exists = find_playlist(original_playlist)
    if playlist_exists[0]:
        playlist = playlist_exists[1]
        playlists[updated_playlist] = playlists[playlist]
        del playlists[playlist]
        return True
    return False

# DELETE

def remove_playlist(target_playlist):
    playlist_exists = find_playlist(target_playlist)
    if playlist_exists[0]:
        playlist = playlist_exists[1]
        del playlists[playlist]
        return True
    return False