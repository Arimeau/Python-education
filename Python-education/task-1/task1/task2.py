str = input('Введите строку - ')
str_len = len(str)
print('Длина строки - ', str_len)
str_price_rub = str_len * 60 // 100
str_price_kop = str_len * 60 % 100
print(f'Стоимость строки: {str_price_rub} р. {str_price_kop} коп.')