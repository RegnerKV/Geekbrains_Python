n = int(input("Введите число от 0 до 9: "))
if -1 < n < 10:
    total: int = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
    print(f"Сумма чисел =  {total}")
else:
    print('Вы ввели неправильное число!')



