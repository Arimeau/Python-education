def div(x,y):
    
    try:
        return x/y

    except ZeroDivisionError:
        return 'Бесконечность'
    
firstValue = input('Введите первое значение ')
secondValue = input('Введите второе значение ')

print(div(int(firstValue),int(secondValue)))