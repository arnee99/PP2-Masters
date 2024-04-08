import requests

singer = input()
numOfSongs = 50
itunes_songs = requests.get(f'https://itunes.apple.com/search?entity=song&limit={numOfSongs}&term=' + singer)
for i in range(numOfSongs):
    if itunes_songs.json()['results'][i]["artistName"] == singer:
        print(itunes_songs.json()['results'][i]["trackName"])