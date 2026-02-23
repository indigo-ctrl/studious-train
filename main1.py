numbers = []
print("Введите 10 целых чисел:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Число {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

# Запись в файл
with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in numbers:
        file.write(f"{num}\n")

print("\nЧисла успешно сохранены в файл 'numbers.txt'")

# TODO: Прочитать числа из файла и выполнить вычисления
read_numbers = []

try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():  # Проверка на пустую строку
                read_numbers.append(int(line.strip()))
except FileNotFoundError:
    print("Файл не найден!")
    exit()
except ValueError:
    print("Ошибка при чтении чисел из файла!")
    exit()

# Вычисления
if read_numbers:
    total_sum = sum(read_numbers)
    average = total_sum / len(read_numbers)
    maximum = max(read_numbers)
    minimum = min(read_numbers)
    
    # Подсчет четных и нечетных
    even_count = sum(1 for num in read_numbers if num % 2 == 0)
    odd_count = len(read_numbers) - even_count
    
    # Вывод результатов
    print(f"\nЧисла из файла: {read_numbers}")
    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
    print(f"Максимум: {maximum}")
    print(f"Минимум: {minimum}")
    print(f"Четных: {even_count}, Нечетных: {odd_count}")
else:
    print("Файл пуст!")
