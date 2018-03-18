file_name = 'learning_python.txt'

print("\nfor printing three times\n")
with open(file_name) as file:
    for lines in file:
        for count in range(3):
            print(lines.strip())

# now for storing lines in a list
with open(file_name) as file:
    lines = file.readlines()
    print("\nfor storing lines in a list\n")

for line in lines:
    print(line.strip())



