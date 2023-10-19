from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import SpotifyOAuth
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ["CLIENT_ID_ENV"] = "fe5e9f4565904b1585c46a860512e1d8"
os.environ["CLIENT_SECRET_ENV"] = "15f90407f3104707b953965af6900573"
user_id = "7ctw1699o8nf0nbrozrbwx82k"
playlist_uri = "03CCcorHAYkbie40rVXblc"
PARAMETER = {
    "name": "Top 100 Songs on Billboard",
    "description": "Going back in time",
    "public": "false"
}
year = "2000-08-12"
HEADER = {
    "Authorization": "Bearer BQDD4BGFheKtVpdGjAkgryqR33_g04GvJpeZXYNXQIiyvUE4BFEB_-bw6jJt0U"
                     "-G1ykdKirmJTA80xWJU96WE6pNbV9mPSIC7gejWE3CWCkurxAaPmHn1hwfBCTMw8M7Uadb9WsMbdx7ub2V_cH89GQdMZqtdmgc-epZ-ovQm8afH9HkbSmCm9JFoi7BzX1b4AoBO3f_xh9la3oBJOxdLdvYu1UmY_UsNQ",
    "Content": "Application/json"
}
endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
time_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{time_travel}/"
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
song_titles = soup.select("li ul li h3")
song_list = [song.getText().strip() for song in song_titles]

spotify_auth = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["CLIENT_ID_ENV"],
                                                         client_secret=os.environ["CLIENT_SECRET_ENV"],
                                                         redirect_uri="http://example.com",
                                                         scope="playlist-modify-private",
                                                         show_dialog=True,
                                                         cache_path="token.txt"
                                                         ))
response = requests.post(url=endpoint, json=PARAMETER, headers=HEADER)
print(response.text)
user_id = spotify_auth.current_user()["id"]
current_user = spotify_auth.current_user()
# song_list = list(map(lambda s: s.strip(), song_list))
# filtered_list = []
# for x in range(len(song_list)):
#     if x != 100:
#         filtered_list.append(song_list[x])
#     else:
#         break
# print(song_list)
uri_list = []

# spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
# result = spotify_auth.search(q="track:Faded year:2000", type="track")
# print(result)
# print(current_user)
# print(user_id)
pp = pprint.PrettyPrinter()
# pp.pprint(uri_list)
song_uris = []
year = year.split("-")[0]
for song in song_list:
    result = spotify_auth.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# pp.pprint(song_uris)

# private_playlist = spotify_auth.user_playlist_create(
#     user=user_id,
#     name=f"{time_travel} Billboard 100",
#     public=False
# )
# print(private_playlist)

add_items = spotify_auth.playlist_add_items(
    playlist_id="7FVDOWOcJzr1xcTzHb0jGt",
    items=song_uris
)
print(add_items)
snapshot_id = "Miw4MzUxNWEyNTg5ZmFjYWI0OTM1OTVhODQwYTM3ZGJlNjQwNzAzYjY3"
