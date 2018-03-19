file_name = 'learning_python.txt'

with open(file_name) as file:
    lines = file.readlines()
    print("\nfor storing lines in a list\n")

for line in lines:
    msg = line.replace("Python","C")
    print(msg.strip())