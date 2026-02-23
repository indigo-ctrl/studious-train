import os

def add_contact():
    """Добавляет контакт (имя и номер) в файл"""
    name = input("Введите имя контакта: ").strip()
    phone = input("Введите номер телефона: ").strip()
    
    if not name or not phone:
        print("Имя и номер не могут быть пустыми!")
        return
    
    # Проверка на существование контакта
    contacts = read_all_contacts()
    if name in contacts:
        print(f"Контакт с именем '{name}' уже существует!")
        return
    
    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {phone}\n")
    print(f"Контакт '{name}' успешно добавлен!")

def read_all_contacts():
    """Читает все контакты из файла и возвращает словарь"""
    contacts = {}
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ": " in line:
                    name, phone = line.strip().split(": ", 1)
                    contacts[name] = phone
    except FileNotFoundError:
        pass  # Файл еще не создан
    return contacts

def write_all_contacts(contacts):
    """Записывает все контакты в файл"""
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")

def show_all_contacts():
    """Выводит все контакты из файла"""
    contacts = read_all_contacts()
    
    if not contacts:
        print("Телефонная книга пуста!")
        return
    
    print("\n--- Все контакты ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print(f"Всего контактов: {len(contacts)}")

def find_contact(name):
    """Ищет контакт по имени"""
    contacts = read_all_contacts()
    
    if name in contacts:
        print(f"Найден контакт: {name}: {contacts[name]}")
    else:
        print(f"Контакт с именем '{name}' не найден!")

def delete_contact(name):
    """Удаляет контакт из файла"""
    contacts = read_all_contacts()
    
    if name in contacts:
        del contacts[name]
        write_all_contacts(contacts)
        print(f"Контакт '{name}' успешно удален!")
    else:
        print(f"Контакт с именем '{name}' не найден!")

def update_contact(name, new_phone):
    """Обновляет номер контакта"""
    contacts = read_all_contacts()
    
    if name in contacts:
        contacts[name] = new_phone
        write_all_contacts(contacts)
        print(f"Номер контакта '{name}' успешно обновлен!")
    else:
        print(f"Контакт с именем '{name}' не найден!")

def main():
    while True:
        print("\n--- Телефонная книга ---")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Обновить контакт")
        print("6. Выход")
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            name = input("Введите имя для поиска: ").strip()
            find_contact(name)
        elif choice == "4":
            name = input("Введите имя для удаления: ").strip()
            delete_contact(name)
        elif choice == "5":
            name = input("Введите имя для обновления: ").strip()
            new_phone = input("Введите новый номер: ").strip()
            update_contact(name, new_phone)
        elif choice == "6":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 6.")

if __name__ == "__main__":
    main()
