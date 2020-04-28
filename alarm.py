import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


# Get username
# ID: mduboef?si=eBdxVVpoQzaCyIdJGIE00A
username = sys.argv[1]
#scope = 'playlist-read-private'

# Erase cashe and ask for user permission
try:
	token = util.prompt_for_user_token(username)
except:
	os.remove(f".cashe-{username}")
	token = util.prompt_for_user_token(username)

app.get('/login', function(req, res) {
var scopes = 'user-read-private user-read-email';
res.redirect('https://accounts.spotify.com/authorize' +
  '?response_type=code' +
  '&client_id=' + my_client_id +
  (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
  '&redirect_uri=' + encodeURIComponent(redirect_uri));
});


spotifyObject = spotipy.Spotify.Spotify(auth=token)

# spotify object
spotifyObject = spotipy.Spotify(auth=token)
