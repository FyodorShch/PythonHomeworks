# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.

# 2) CRUD: Create, Read, Update, Delete

# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

phonebook = []

# fio = [{'surname': 'Ivanov', 'name': 'Ivan', 'phone': '1781841', 'discription': 'worker'}, {
#     'surname': 'Petrov', 'name': 'Vasiliy', 'phone': '145546158', 'discription': 'student'}]

def create(db: list):  # data_base
    db.append(get_user_data())   
    return db

def view_file(db: list) -> None:
    for i in db:
        print(i['surname'], i['name'], i['phone'], i['description'])

def read(db: list):
    surname = input()
    j = 0
    for i in db:
        if i['surname'].startswith(surname):
            print(db[j])
        j=j+1

def get_user_data():
    return {'surname': input("Введите фамилию"),
        'name': input("Введите имя"),
        'phone': input("Введите номер телефона"),
        'description': input("Введите описание")}

def import_file(file_path: str) -> list:
    data = []
    # r тип операции - чтение
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:  # перебор строк в файле + \n
            new_list = string.strip().split(",")  # убираем перенос строки и делим по запятой
            data.append({"surname": new_list[0], 'name': new_list[1], 'phone': new_list[2], 'description': new_list[3]})
    return data

def export_file(file_path: str, db: list) -> list:
    with open(file_path, "w", encoding='utf-8') as file:
        for el in db:  # перебор строк в файле + \n
            file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")

def change_person(db: list):
    i = int(input("Введите пользователя для замены данных: "))
    j = str(input("Введите что хотите заменить: "))
    db[i][j] = input()

def delete_element(db: list):
    i = int(input("Выберите пользователя для удаления"))
    db.pop(i)

def menu(db: dict) -> None:
    print("Возможные действия")
    print("1. Создать запись")
    print("2. Получить запись по фамилии")
    print("3. Вывод всех абонентов")
    print("4. Импорт файла")
    print("5. Экспорт файла")
    print("6. Изменение данных")
    print("7. Удаление пользователя")
    print("8. Выход")
    while True:
        user_input = input("Введите действие > ")
        if user_input == '1':
            create(db)
        if user_input == '2':
            read(db)
        if user_input == '3':
            view_file(db)
        if user_input == '4':
           file = 'hw8/data.txt'
           db = import_file(file) 
        if user_input == '5':
            file = 'hw8/data.txt'
            export_file(file, db)
        if user_input == '6':
            change_person(db)
        if user_input == '7':
            delete_element(db)
        if user_input == '8':
            break

menu(phonebook)