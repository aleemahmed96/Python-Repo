filename = "loop.txt"
active = True
with open(filename,'a') as file:
    while(active):
        reason = input("Why do you like Python?")
        file.write("\n" + reason)
        if reason == "q":
            active = False

with open(filename,"r") as file:
    lines = file.readlines()
    file.close()

with open(filename,"w") as file:
    for line in lines:
        if line!="q":
            file.write(line)
            print(line.strip())
    
            