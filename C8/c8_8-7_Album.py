#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary containing these
# two pieces of information. Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.




def make_album (a, b):
    """Create an album"""
    artist_album = []
    for dict_counter in range (0,3):
        artist = input("Enter the artist name: ")
        album = input("Enter the album name: ")


        new_artist_album = {'artist_name': artist, 'album_name': album}
        artist_album.append(new_artist_album)


    return artist_album

discographies = make_album('','')

print (discographies)



#def make_album (a, b):
#    """Create an album"""
#    #artist = input ("Enter the artist name: ")
#    album = input("Enter the album name: ")
#    artist_album = {'artist_name':a, 'album_name':album}

#    return artist_album

#discographies = make_album('x','y')

#print (discographies)
