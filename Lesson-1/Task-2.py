time = int(input('Введите время в секундах: '))
string = f'Время: {time // 3600}:{time % 3600 // 60}:{time % 3600 % 60}'

print(string)
