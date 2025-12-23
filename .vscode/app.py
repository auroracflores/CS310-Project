from flask import Flask, render_template, request
import pandas as pd
import main as merge
from flask import session
app = Flask(__name__)
app.secret_key = "dev_key"

# Load the dataset once when the app starts
#df = pd.read_csv("C:\\Users\\BM\\OneDrive\\Documents\\CS310\\Playlist Sorting CS310\\.vscode\\data\\dataset.csv")
df = pd.read_csv("spotify_track_clean.csv")
def make_playlist(genre, vibe, n_songs=20):
    playlist = df.copy()

    # Filter by genre or not if chosen "all"
    if genre and genre != "all":
        playlist = playlist[playlist["track_genre"] == genre]

    # Filter by vibe using energy/valence as a proxy
    if vibe == "Upbeat":
        playlist = playlist[(playlist["energy"] > 0.6) &
                             (playlist["valence"] > 0.5) &
                             (playlist["tempo"] > 0.5)]
    elif vibe == "Chill":
        playlist = playlist[(playlist["energy"] < 0.5) &
                            (playlist["valence"] > 0.4) & #make valence between .4 and .8
                             (playlist["valence"] < 0.8) &
                             (playlist["acousticness"] > 0.5)]
    elif vibe == "Moody":
        playlist = playlist[(playlist["energy"] < 0.5) &
                             (playlist["valence"] < 0.4) &
                             (playlist["tempo"] < 0.5)]
    elif vibe == "Party":
        playlist = playlist[(playlist["energy"] > 0.7) &
                             (playlist["tempo"] > 0.5) &
                             (playlist["danceability"] > 0.6)]

    # Random sample of songs
    if len(playlist) > n_songs:
        playlist = playlist.sample(n_songs)

    # Add a Spotify URL column (track_id -> URL)
    playlist = playlist.copy()
    playlist["spotify_url"] = "https://open.spotify.com/track/" + playlist["track_id"]

    # Return only the columns 
    return playlist[["track_name", "artists", "track_genre", "spotify_url"]]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    sort_by = request.form.get("sort")

    if "songs" not in session:
        genre = request.form.get("genre")
        vibe = request.form.get("vibe")

        playlist = make_playlist(genre, vibe)
        session["songs"] = playlist.to_dict(orient="records")

    songs = session["songs"]

    if sort_by == "track":
        merge.mergeSort(songs, 0, len(songs) - 1, merge.mergeTrack)
    elif sort_by == "artist":
        merge.mergeSort(songs, 0, len(songs) - 1, merge.mergeArtist)
    songs = session["songs"] # Save new song order
    return render_template("results.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)
