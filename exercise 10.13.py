import json
filename = 'username.json' 

def get_stored_username():
    """Get stored username if available."""
    
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username




def get_new_username():
    """Prompt for a new username."""

    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username



def greet_user():
    """Greet the user by name."""

    username = get_stored_username()
    if username:
        print("Is this your name \"" + username + "\"?")
        msg = input("Tell with 'y' for yes and 'n' for no. " )
        if msg == "y":
            print("Welcome back " + username + "!")
        if msg == "n":
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("you entered wrong command. Tell again! ")

greet_user()