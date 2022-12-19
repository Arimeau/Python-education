with open('f:\Code\Python-education\practice-10\data.txt') as file:
    strings = file.readlines()
    for i in range(len(strings)):
        print(strings[len(strings) - 1 - i].strip())