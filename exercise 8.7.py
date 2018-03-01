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