file1 = 'greeting_name.txt'
with open(file1, 'w') as file_object:
    active = True
    delete_word= 'quit'
    while active:
        sample= input('write your name ')
        file_object.write('greetings ' + sample + "\n")
        if sample == 'quit':
            acitve = False
            break
            

"""other way of doing it is this"""

greeting_name = open(file1, 'r')
lines = greeting_name.readlines()
greeting_name.close()

greeting_name = open (file1,'w')
for line in lines:
    if line!="greetings quit\n":
        greeting_name.write(line)
        print(line.strip("\n"))



