n = int(input('Введите число: '))

i = 0
list = []
while i < n:

    current = []
    i+=1
    # list.append(i)
    j = 0
    while j < i:
        j+=1
        current.append(j)

    list.append(current)

for item in list:
    print(item)