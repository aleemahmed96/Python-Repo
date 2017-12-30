CURRENT_USER = ['sadiq', 'sheeraz', 'noman', 'Kashif', 'ovais']
NEW_USER = ['Ovais', 'KASHIF', 'ahmed', 'faraz', 'rehan']

for new in NEW_USER:
    if new.capitalize() in CURRENT_USER or new.lower() in CURRENT_USER:
        print('please change your name')
    else:
        print('Welcome')