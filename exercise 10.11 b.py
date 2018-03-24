import json

filename ="fav_number.json"
with open(filename, mode='r') as file:
    msg = json.load(file)
    
print("I know your favourite number. It's ",msg)