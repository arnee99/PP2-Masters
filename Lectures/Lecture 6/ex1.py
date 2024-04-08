artists = ['Sting', 'Bruno Mars', 'Nikolay Baskov', 'Kairat Nurtas']
songs = ['Shape of my heart', 'Grenade', 'Натуральный блондин', 'Алматы түні']

playlist = {}

for i in range(len(artists)):
    playlist[artists[i]] = songs[i]

# CSV - Comma Separated Values
f = open('singer.csv', 'w')
for artist in artists:
    f.write(f"{artist}, {playlist[artist]}" + '\n')
f.close()    
    
with open('singer.csv', 'r') as file_reader:
    compositions = file_reader.read()
print(compositions)