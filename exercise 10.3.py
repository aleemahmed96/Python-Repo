filename = "guest.txt"

with open(filename,"w") as file:
    msg = input("give your name here: \t")
    file.writelines(msg)
    file.close()

