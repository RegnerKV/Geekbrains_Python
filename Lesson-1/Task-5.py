profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма приносит прибыль. Рентабельность выручки составляет: {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сторудника составляет {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма убыточна")