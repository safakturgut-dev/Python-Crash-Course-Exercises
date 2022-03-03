# 8-8
def make_album(artist, title, song_count=None):
    album = {'artist': artist, 'album_title': title}
    if song_count:
        album['number_of_songs'] = song_count
    return album


print('Enter the information about an album and i will create a dictionary.')
print('Enter \'q\' for quit.')

while True:
    artist = input('Enter the name of artist: ')

    if artist == 'q':
        break

    album_title = input('Enter the name of album: ')

    if album_title == 'q':
        break

    print(make_album(artist, album_title))
