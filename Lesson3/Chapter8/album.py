def makeAlbum(artistName, albumTitle):
    music = {'Artist' : artistName, 'Album': albumTitle}
    return music


while True:
    artist = input('What is the Artists Name? ')
    album = input('What is the albums name? ')
    albumDict = {}

    albumDict = makeAlbum(artist, album)

    print(albumDict)

    again = input('would you like to make another album? (type q to quit)' )
    if again == 'q':
        break
