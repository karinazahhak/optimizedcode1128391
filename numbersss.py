# Пустой список чисел
numbers = []

# Ввод 5 чисел
print("Введите 5 чисел.")
for i in range(5):
    x = int(input("Введите число:"))
    numbers.append(x)

# Ваши числа, мин. число, макс. число
print("Ваши числа: ", numbers)
max = max(numbers)
min = min(numbers)

# Сумма чисел и её переменная
sum = 0
for x in numbers:
    sum = sum + x

print("Максимальное число: ", max)
print("Минимальное число: ", min)
print('Сумма чисел: ', sum)