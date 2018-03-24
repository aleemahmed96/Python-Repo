import json

prompt = input("Enter your favourite number: ")
filename = "fav_number.json"
with open(filename,'w') as file:
    json.dump(prompt,file)
