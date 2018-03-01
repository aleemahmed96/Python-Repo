#Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.

def make_album(artist_name,album_title):
    """generating dictionary that describes about the music album"""

    dictionary={"Artist name":artist_name,"Album title":album_title }
    return dictionary


count =0
for count in range(3):
    print("enter artist name")
    artist_name=input("artist name: ")
    print("enter album title")
    album_title=input("album title: ")
    signal = make_album(artist_name,album_title)
    print(signal)

#Add an optional parameter to make_album() that allows you to store the
#number of tracks on an album. If the calling line includes a value for the number
#of tracks, add that value to the album’s dictionary. Make at least one new
#function call that includes the number of tracks on an album.

def make_album_with_track(artist_name,album_title,album_track=''):
    """generating dictionary that describes about the music album"""

    if album_track=="":
        dictionary={"Artist name":artist_name,"Album title":album_title }
    else:
        dictionary={"Artist name":artist_name,"Album title":album_title,"Album tracks":album_track }
    return dictionary


count =0
for count in range(3):
    print("enter artist name")
    artist_name=input("artist name: ")
    print("enter album title")
    album_title=input("album title: ")
    print("enter album track")
    album_track=input("album track: ")
    signal = make_album_with_track(artist_name,album_title,album_track)
    print(signal)