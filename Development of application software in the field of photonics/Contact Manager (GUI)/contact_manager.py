from dataclasses import dataclass
from typing import Optional
from functools import wraps
from collections import defaultdict

@dataclass
class Contact:  # базовый класс для контакта
    phone_number: str  # номер телефона
    name: str  # имя контакта в базе
    group: Optional[str] = None  # принадлежность контакта к определённой группе

def check_unique(func):  # декоратор, проверяющий по одному образцу уникальность как номера, так и имени
    @wraps(func)
    def wrapper(self, contact, *args, **kwargs):
        if contact.phone_number in self.phone_numbers:  # проверка на совпадение номера
            print(f"Контакт с номером {contact.phone_number} уже существует.")
            return False
        if contact.name in self.names:  # проверка на совпадение имени
            print(f"Контакт с именем {contact.name} уже существует.")
            return False
        return func(self, contact, *args, **kwargs)
    return wrapper

class ContactManager:
    def __init__(self):
        self.groups = defaultdict(list)  # словарь для групп контактов
        self.contacts = {}  # словарь для всех контактов (ключ - кортеж (phone_number, name))
        self.phone_numbers = {}  # словарь для проверки уникальности номеров
        self.names = {}  # словарь для проверки уникальности имен

    @check_unique
    def add_contact(self, contact: Contact):
        self.groups[contact.group].append(contact)  # недостающая группа будет автоматически создана
        self.contacts[(contact.phone_number, contact.name)] = contact # добавление в словарь контактов
        self.phone_numbers[contact.phone_number] = contact # добавление в список номеров
        self.names[contact.name] = contact # добавление в список имён
        return True

    def change_contact_name(self, phone_number: str, new_name: str):
        """Изменяет имя контакта с указанным номером."""

        # Находим контакт по номеру телефона
        contact = None
        for key, c in self.contacts.items():
            if c.phone_number == phone_number:
                contact = c
                break

        if not contact:
            return False  # Контакт не найден

        # Проверяем, нет ли уже контакта с таким именем
        if new_name in self.names:
            return False  # Контакт с таким именем уже существует

        # Удаляем старый контакт из всех списков
        old_key = (contact.phone_number, contact.name)
        del self.contacts[old_key]
        del self.names[contact.name]

        # Обновляем имя контакта и создаём новый ключ
        contact.name = new_name
        new_key = (contact.phone_number, new_name)

        # Добавляем контакт обратно в словари
        self.contacts[new_key] = contact
        self.names[new_name] = contact
        return True  # Имя успешно изменено

    def change_group(self, phone_number: str, new_group: str):  # изменение группы, соответствующей контакту
        contact = None
        # поиск контакта по номеру телефона
        for c in self.contacts.values():
            if c.phone_number == phone_number:
                contact = c
                break
        if contact:
            if contact.group:  # если группа была, убираем контакт из старой группы
                self.groups[contact.group].remove(contact)
                if not self.groups[contact.group]:
                    del self.groups[contact.group]  # удаление группы, если она пуста

            contact.group = new_group  # присвоение новой группы контакту
            if new_group not in self.groups:
                self.groups[new_group] = []  # создание новой группы, если её нет
            self.groups[new_group].append(contact)  # добавляем контакт в новую группу
            return True
        return False

    def format_phone_number(self, phone_number: str) -> str:
        phone_str = phone_number.strip()  # удаляем возможные пробелы
        if len(phone_str) == 11:  # преобразуем номер, введённый в формате 8800...
            if phone_str[0] == '8':  # если номер начинается с 8
                phone_str = '7' + phone_str[1:]  # заменяем 8 на 7
            return f"+{phone_str[0]}({phone_str[1:4]}){phone_str[4:7]}-{phone_str[7:9]}-{phone_str[9:11]}"

        if len(phone_str) == 12:  # преобразуем номер, введённый в формате 375...
            return f"+{phone_str[0:3]}({phone_str[3:5]}){phone_str[5:8]}-{phone_str[8:10]}-{phone_str[10:]}"

        return phone_str  # Если номер не 11 или 12 знаков, просто возвращаем его без изменений


    def list_contacts(self, group_index: int = 0):
        print("--------------------")
        print("КОНТАКТЫ")
        print("--------------------")

        if group_index == 0: # вывод списка контактов
            if self.contacts:
                for index, contact in enumerate(self.contacts.values(), 1):
                    formatted_number = self.format_phone_number(contact.phone_number)
                    print(f"{index}. {contact.name} ({formatted_number}) - {contact.group}")
                self.edit_or_delete_contact()
            else: # если список контактов на данный момент пуст
                print("Пусто. Давайте создадим контакт!")
        else:
            group_names = list(self.groups.keys())
            try:
                group_index = int(group_index)
                if 1 <= group_index <= len(group_names):
                    selected_group = group_names[group_index - 1]
                    contacts_in_group = self.groups[selected_group]
                    if contacts_in_group:
                        print(f"Контакты в группе {selected_group}:")
                        for index, contact in enumerate(contacts_in_group, 1):
                            formatted_number = self.format_phone_number(contact.phone_number)
                            print(f"{index}. {contact.name} ({formatted_number})")
                        self.edit_or_delete_contact()
                    else:
                        print(f"В группе {selected_group} нет контактов.")
                else:
                    print("Неверный номер группы.")
            except ValueError:
                print("[!!!] Введен некорректный номер.")

    def input_new_contact(self):  # метод для ввода нового контакта
        name = input("Введите имя контакта: ")
        while True:
            phone_number = input("Введите номер телефона: ").strip()
            if phone_number.isdigit(): # проверка, что введённый номер является строкой, и что он состоит только из цифр
                break
            else:
                print("[!!!] Номер должен быть целым числом!")

        group = input("Введите группу контакта (по желанию, если не нужно - оставьте пустым): ")
        group = group if group else None
        contact = Contact(phone_number, name, group)

        contact.phone_number = self.format_phone_number(contact.phone_number) # форматирование номера перед добавлением контакта

        if self.add_contact(contact):
            print("Контакт добавлен успешно!")
        else:
            print("[!!!] Ошибка, контакт не добавлен!")

    def edit_or_delete_contact(self):
        try:
            action = input("Чтобы выйти в главное меню, введите m. \nЧтобы отредактировать информацию о контакте, введите его порядковый номер: ").strip()
            if action.lower() == 'm':
                return
            action = int(action)

            if action <= 0 or action > len(self.contacts):
                print("[!!!] Неверный выбор контакта!")
                return

            contact = list(self.contacts.values())[action - 1]
            print(f"Вы выбрали: {contact.name} ({contact.phone_number})")

            edit_action = input(
                "Что хотите сделать? (1) Изменить имя, (2) Изменить номер, (3) Изменить группу, (4) Удалить, (q) Отмена: ").strip()

            if edit_action == '1':
                new_name = input("Введите новое имя: ")
                self.change_contact_name(contact.phone_number, new_name)
                print(f"Имя контакта изменено на {new_name}")
            elif edit_action == '2':
                new_phone_number = input("Введите новый номер телефона: ")
                contact.phone_number = self.format_phone_number(new_phone_number)
                print(f"Номер телефона изменен на {contact.phone_number}")
            elif edit_action == '3':
                new_group = input("Введите новую группу: ")
                self.change_group(contact.phone_number, new_group)
                print(f"Группа изменена на {new_group}")
            elif edit_action == '4':
                self.delete_contact(contact.phone_number)
            elif edit_action.lower() == 'q':
                return
            else:
                print("[!!!] Неверный выбор.")
        except ValueError:
            print("[!!!] Введен некорректный номер.")

    def delete_contact(self, phone_number: str): # удаление контакта по номеру телефона
        contact = None
        for c in self.contacts.values():
            if c.phone_number == phone_number:
                contact = c
                break
        if contact:
            del self.contacts[(contact.phone_number, contact.name)]
            del self.phone_numbers[contact.phone_number]
            del self.names[contact.name]

            if contact.group:  # удаляем контакт из группы
                self.groups[contact.group].remove(contact)
                if not self.groups[contact.group]:  # если группа пустая, удаляем её
                    del self.groups[contact.group]

            print(f"Контакт {contact.name} с номером {contact.phone_number} удален.")
        else:
            print("[!!!] Контакт не найден.")


def main():
    manager = ContactManager()

    while True:
        print("\n[МЕНЕДЖЕР КОНТАКТОВ]")
        print("[1] Создать новый контакт")
        print("[2] Показать полный список контактов")
        print("[3] Показать список групп")
        print("[4] Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            manager.input_new_contact()

        elif choice == '2': # полный список контактов
            manager.list_contacts()


        elif choice == '3': # показываем список групп и даём выбрать группу для просмотра
            if manager.groups:
                print("Доступные группы:")
                group_names = list(manager.groups.keys())
                for index, group in enumerate(group_names, 1):
                    print(f"[{index}] {group}")
                try: # запрос номера группы для показа её контактов
                    group_index = int(input("Введите номер группы для просмотра контактов: "))
                    if 1 <= group_index <= len(group_names):
                        selected_group = group_names[group_index - 1]
                        contacts_in_group = manager.groups[selected_group]
                        if contacts_in_group:
                            print(f"Контакты в группе {selected_group}:")
                            for contact in contacts_in_group:
                                formatted_number = manager.format_phone_number(contact.phone_number)
                                print(f"  {contact.name} ({formatted_number})")
                        else:
                            print(f"В группе {selected_group} нет контактов.")
                    else:
                        print("Неверный номер группы.")
                except ValueError:
                    print("[!!!] Введен некорректный номер.")
            else:
                print("Групп ещё нет. Чтобы создать группу, пропишите её при создании нового контакта.")
        elif choice == '4':
            print("Выход...")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
