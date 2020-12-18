a = int(input("Введите результаты пробежки первого дня (в км): "))
b = int(input("Введите желаемый результат пробежки (в км): "))
days = 1
distance = a
while distance < b:
        a = a + 0.1 * a
        days += 1
        distance = distance + a
print(f"Вы достигнете желаемого результата на {days} день")