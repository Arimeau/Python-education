a = int(input('Введите число a - '))
b = int(input('Введите число b - '))

if b == 0:
    print('Введение нуля неприемлемо')
    quit()
else:
    sum = a + b
    sub = a - b
    myl = a * b
    div = a / b
    integer = a // b
    rem = a % b
    sqrt = (((a ** 10)+(b ** 10)) ** 0.5)

print('sum', sum)
print('sub', sub)
print('myl', myl)
print('div', div)
print('integer', integer)
print('rem', rem)
print('sqrt', sqrt)