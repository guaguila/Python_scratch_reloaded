#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allow users to enter an album’s
# artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

    #Loop to capture users album artist and title
    #With the captured information, call make_album and print the dictionary
    #Include quit value


def make_album (something):
    """Print the album"""
    #print (artist_album.count())
    for record in something:
        print ("\nArtist: " , record['artist_name'].title()
               + "\nAlbum: ", record['album_name'].title())

    #print(artist_album)
    #print(len(artist_album)) # imprime el tamaño de la lista

artist_album = []
while True:
    print("(Enter 'q' at any time to quit)")
    artist = input("Enter the artist name: ")
    if artist == 'q':
        break

    album = input("Enter the album name: ")
    if album == 'q':
        break

    new_artist_album = {'artist_name': artist, 'album_name': album}
    artist_album.append(new_artist_album)


make_album(artist_album)


