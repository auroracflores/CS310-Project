from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset once when the app starts
df = pd.read_csv("C:\\Users\\BM\\OneDrive\\Documents\\CS310\\Playlist Sorting CS310\\.vscode\\data\\dataset.csv")

def make_playlist(genre, vibe, n_songs=20):
    playlist = df.copy()

    # Filter by genre
    if genre:
        playlist = playlist[playlist["track_genre"] == genre]



    # Filter by vibe using energy/valence as a proxy
    if vibe == "Upbeat":
        playlist = playlist[(playlist["energy"] > 0.6) & (playlist["valence"] > 0.5)]
    elif vibe == "Chill":
        playlist = playlist[(playlist["energy"] < 0.5) & (playlist["valence"] < 0.6)]

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
    genre = request.form.get("genre")
    vibe = request.form.get("vibe")

    playlist = make_playlist(genre, vibe)

    # Convert to list of dicts so Jinja can loop easily
    songs = playlist.to_dict(orient="records")

    return render_template("results.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)
