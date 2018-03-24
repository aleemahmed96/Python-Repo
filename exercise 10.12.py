import json
filename = "fav_number.json"

def user_input_fav_number():
    """to input the user favourite number
    """

    prompt = input("Enter your favourite number: ")
    with open(filename,'w') as file:
        json.dump(prompt,file)
    print("We will tell you your favourite number when you open this program later.")


def stored_fav_number():
    """"if number is already stored
    """
    with open(filename, mode='r') as file:
        msg = json.load(file)
    return msg

def show_fav_number():
    msg = stored_fav_number()
    if msg:
        print("You have already told your favourite number. It's ",msg)
    else:
        user_input_fav_number()

show_fav_number()


