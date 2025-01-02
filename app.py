from flask import Flask, jsonify
from song_operations import add_song, read_song, edit_song, remove_song
from playlist_operations import read_playlist, edit_playlist, remove_playlist

app = Flask(__name__)

# Song CRUD routes

@app.route('/')
def home():
    return 'Welcome to the playlist management API!'

# POST - add_song()

@app.route('/songs/<string:playlist>/<string:song>', methods=['POST'])
def create_song(playlist, song): # Also includes functionality to add a playlist
    add_song(playlist, song)
    data = { "message": "Song created!" }
    return jsonify(data)

# GET - read_song()

@app.route('/songs/<string:song>', methods=['GET'])
def get_song(song):
    message = read_song(song)
    data = { "message": message } if message else { "message": "Song not found." }
    return jsonify(data)

# PUT - edit_song()

@app.route('/songs/<string:original_song>/<string:updated_song>', methods=['PUT'])
def update_song(original_song, updated_song):
    song_exists = edit_song(original_song, updated_song)
    data = { "message": "Song updated!" } if song_exists else { "message": "Song not found." }
    return jsonify(data)

# DELETE - remove_song()

@app.route('/songs/<string:song>', methods=['DELETE'])
def delete_song(song):
    song_exists = remove_song(song)
    data = { "message": "Song removed!" } if song_exists else { "message": "Song not found." }
    return jsonify(data)

# Playlist CRUD routes

# GET - read_playlist()

@app.route('/playlists/<string:playlist>', methods=['GET'])
def get_playlist(playlist):
    message = read_playlist(playlist)
    data = { "message": message } if message else { "message": "Playlist not found." }
    return jsonify(data)

# PUT - edit_song()

@app.route('/playlists/<string:original_playlist>/<string:updated_playlist>', methods=['PUT'])
def update_playlist(original_playlist, updated_playlist):
    playlist_exists = edit_playlist(original_playlist, updated_playlist)
    data = { "message": "Playlist updated!" } if playlist_exists else { "message": "Playlist not found." }
    return jsonify(data)

# DELETE - remove_playlist()

@app.route('/playlists/<string:playlist>', methods=['DELETE'])
def delete_playlist(playlist):
    playlist_exists = remove_playlist(playlist)
    data = { "message": "Playlist removed!" } if playlist_exists else { "message": "Playlist not found." }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)