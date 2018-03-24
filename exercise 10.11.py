import json

prompt = input("Enter your favourite number: ")
filename = "fav_number.json"
with open(filename,'w') as file:
    json.dump(prompt,file)

with open(filename, mode='r') as file:
    msg = json.load(file)
    
print("I know your favourite number. It's ",msg)
