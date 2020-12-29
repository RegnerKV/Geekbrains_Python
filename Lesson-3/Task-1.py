def my_func():
    try:
        x = int(input('Введите число: '))
        y = int(input('Введите число: '))
    except ZeroDivisionError:
        return
    z = x / y
    return z

z = my_func()
print(z)