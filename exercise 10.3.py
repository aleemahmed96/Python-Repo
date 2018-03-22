filename = "guest.txt"

with open(filename,"a") as file:
    msg = input("give your name here: ")
    file.writelines("\n" + msg)
    file.close()

