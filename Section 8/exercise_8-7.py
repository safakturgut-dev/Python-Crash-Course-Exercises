# 8-7
def make_album(artist, title, song_count=None):
    album = {'artist': artist, 'album_title': title}
    if song_count:
        album['number_of_songs'] = song_count
    return album


print(make_album('adele', '21'))
print(make_album('ed sheeran', 'divide'))
print(make_album('taylor swift', 'love', 18))
