#list of people who should take the favorite languages poll

favorite_languages = {
    'Sheeraz': 'python',
    'Sadiq': 'c',
    'Kashif': 'ruby',
    'Furqan': 'python',
}

#Included some names that are already in the dictionary and some that are not.
friends = {'Sheeraz':'pyhton', 'Sadiq':'c', 'Kashif':'ruby', 'Furqan':'python', 'Wahaj':'c++', 'Ovais':'php', 'Usman':'java'}
favorite_languages.update(friends)
for name in favorite_languages.keys():
    if name in friends:
        print(" Hi " + name.title() +", I see your favorite language is " + favorite_languages[name].title() + "!")
    else:
        print("kahan se ajate ho tm log???" + favorite_languages.keys())

#Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.

people= {'Sheeraz':'yes', 'Sadiq':'yes', 'Kashif':'not polled', 'Furqan':'no'}
for person,poll in people.items():
    if poll == 'yes' or poll == 'no':
        print("thanks for polling " + poll + " " + person)
    else:
        print("please poll")