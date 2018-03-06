#Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name,album_title):
    """generating dictionary that describes about the music album"""

    dictionary={"Artist name":artist_name,"Album title":album_title }
    return dictionary
    print(dictionary)

count=0
while (count<3):
    print("press \"q\" to quit")
    print("enter artist name")
    artist_name=input("artist name: ")
    if artist_name=="q":
        break
    print("enter album title")
    album_title=input("album title: ")
    if album_title=="q":
       break
    signal = make_album(artist_name,album_title)
    print(signal)
    count=count+1
