import csv

def read_all_students():
    """Читает всех студентов из файла и возвращает словарь {имя: список оценок}"""
    students = {}
    try:
        with open("grades.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ": " in line:
                    name, grades_str = line.strip().split(": ", 1)
                    # Преобразуем строку с оценками в список целых чисел
                    grades = [int(g.strip()) for g in grades_str.split(",") if g.strip().isdigit()]
                    students[name] = grades
    except FileNotFoundError:
        pass  # Файл еще не создан
    except ValueError:
        print("Ошибка при чтении файла с оценками!")
    return students

def write_all_students(students):
    """Записывает всех студентов в файл"""
    with open("grades.txt", "w", encoding="utf-8") as file:
        for name, grades in students.items():
            grades_str = ", ".join(map(str, grades))
            file.write(f"{name}: {grades_str}\n")

def add_student():
    """Добавляет нового студента с оценками"""
    name = input("Введите фамилию и имя студента: ").strip()
    
    if not name:
        print("Имя не может быть пустым!")
        return
    
    students = read_all_students()
    
    if name in students:
        print(f"Студент '{name}' уже существует!")
        return
    
    # Ввод оценок
    grades_input = input("Введите оценки через пробел: ").strip()
    try:
        grades = [int(g) for g in grades_input.split()]
        # Проверка допустимости оценок (обычно от 2 до 5)
        if not all(2 <= g <= 5 for g in grades):
            print("Оценки должны быть от 2 до 5!")
            return
    except ValueError:
        print("Ошибка! Введите целые числа через пробел.")
        return
    
    students[name] = grades
    write_all_students(students)
    print(f"Студент '{name}' успешно добавлен с оценками {grades}")

def add_grade(name, grade):
    """Добавляет оценку существующему студенту"""
    students = read_all_students()
    
    if name in students:
        if 2 <= grade <= 5:
            students[name].append(grade)
            write_all_students(students)
            print(f"Оценка {grade} добавлена студенту '{name}'")
        else:
            print("Оценка должна быть от 2 до 5!")
    else:
        print(f"Студент '{name}' не найден!")

def show_all_students():
    """Выводит всех студентов и их средний балл"""
    students = read_all_students()
    
    if not students:
        print("Журнал успеваемости пуст!")
        return
    
    print("\n--- Журнал успеваемости ---")
    for name, grades in students.items():
        avg = sum(grades) / len(grades) if grades else 0
        print(f"{name}: {grades} средний: {avg:.1f}")

def find_students_below(threshold):
    """Ищет студентов с оценкой ниже порога"""
    students = read_all_students()
    
    if not students:
        print("Журнал успеваемости пуст!")
        return
    
    found = False
    print(f"\nСтуденты с оценкой ниже {threshold}:")
    for name, grades in students.items():
        below = [g for g in grades if g < threshold]
        if below:
            print(f"{name}: проблемные оценки {below}")
            found = True
    
    if not found:
        print(f"Студентов с оценкой ниже {threshold} не найдено")

def calculate_group_statistics():
    """Выводит статистику по группе"""
    students = read_all_students()
    
    if not students:
        print("Журнал успеваемости пуст!")
        return
    
    # Собираем все оценки
    all_grades = []
    student_averages = {}
    
    for name, grades in students.items():
        all_grades.extend(grades)
        if grades:
            student_averages[name] = sum(grades) / len(grades)
    
    if not all_grades:
        print("Нет оценок для расчета статистики!")
        return
    
    # Общая статистика
    group_avg = sum(all_grades) / len(all_grades)
    
    # Лучший и худший студенты
    best_student = max(student_averages, key=student_averages.get)
    worst_student = min(student_averages, key=student_averages.get)
    
    print("\n--- Статистика по группе ---")
    print(f"Количество студентов: {len(students)}")
    print(f"Всего оценок: {len(all_grades)}")
    print(f"Средний балл группы: {group_avg:.2f}")
    print(f"Лучший студент: {best_student} (средний балл {student_averages[best_student]:.2f})")
    print(f"Худший студент: {worst_student} (средний балл {student_averages[worst_student]:.2f})")

def save_to_csv(filename):
    """Экспорт данных в CSV формат"""
    students = read_all_students()
    
    if not students:
        print("Нет данных для экспорта!")
        return
    
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Заголовки
            writer.writerow(['ФИО', 'Оценки', 'Средний балл'])
            
            for name, grades in students.items():
                avg = sum(grades) / len(grades) if grades else 0
                grades_str = ', '.join(map(str, grades))
                writer.writerow([name, grades_str, f"{avg:.2f}"])
        
        print(f"Данные успешно экспортированы в файл '{filename}'")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def main():
    while True:
        print("\n--- Журнал успеваемости ---")
        print("1. Добавить студента")
        print("2. Добавить оценку студенту")
        print("3. Показать всех студентов")
        print("4. Найти студентов с низкими оценками")
        print("5. Показать статистику группы")
        print("6. Экспортировать в CSV")
        print("7. Выход")
        
        choice = input("Выберите действие (1-7): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            name = input("Введите имя студента: ").strip()
            try:
                grade = int(input("Введите оценку (2-5): ").strip())
                add_grade(name, grade)
            except ValueError:
                print("Ошибка! Введите целое число.")
        elif choice == "3":
            show_all_students()
        elif choice == "4":
            try:
                threshold = int(input("Введите пороговое значение: ").strip())
                find_students_below(threshold)
            except ValueError:
                print("Ошибка! Введите целое число.")
        elif choice == "5":
            calculate_group_statistics()
        elif choice == "6":
            filename = input("Введите имя CSV файла (например, grades.csv): ").strip()
            if not filename.endswith('.csv'):
                filename += '.csv'
            save_to_csv(filename)
        elif choice == "7":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 7.")

if __name__ == "__main__":
    main()
