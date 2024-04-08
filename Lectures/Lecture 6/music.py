import requests

singer = input()
numOfSongs = 1
itunes_songs = requests.get('https://itunes.apple.com/search?entity=song&limit={numOfSongs}&term={singer}')
for i in range(numOfSongs):
    if itunes_songs.json()['results'][i]["artistName"] == singer:
        print(itunes_songs.json()['results'][i]["trackName"])