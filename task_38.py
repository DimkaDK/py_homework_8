"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""

# Добавление данных
def add_new_data():
    print("Введите новые данные в формате: Фамилия Имя Отчество Телефон: ")
    with open("phonebook.txt", "a", encoding = "UTF-8") as saved_data:
        saved_data.writelines(input())
        saved_data.write("\n")
    print("Ok")

# Поиск данных по параметру
def find_data(parametr):
    with open("phonebook.txt", "r", encoding = "UTF-8") as saved_data:
        for line in saved_data:
            if parametr in line:
                print(line)

# Запрос параметра для поиска
def ask_parametr():
    parametr = str(input("Введите запрос: "))
    return parametr

# Изменение данных
def change_data():
    with open("phonebook.txt", "r", encoding = "UTF-8") as saved_data:
        file = saved_data.read()
        
    with open("phonebook.txt", "w", encoding = "UTF-8") as saved_data:
        file = file.replace(input("Что меняем: "), input("На что меняем: "))
        saved_data.write(file)      
    
                

# Удаление данных
def delete_data():
    with open("phonebook.txt", "r", encoding = "UTF-8") as saved_data:
        file = saved_data.read()
        
    with open("phonebook.txt", "w", encoding = "UTF-8") as saved_data:
        file = file.replace(input("Что удаляем: "), " ")
        saved_data.write(file)
   


# find_data(ask_parametr())
# add_new_data()
# change_data()
# delete_data()

print("Вас приветствует телефонный Справочник")
i = int(input("Введите требуемое действие: 1 - для добавления записей; 2 - для поиска записей; 3 - для изменения записей; 4 - для удаления записей: "))
if i == 1: add_new_data()
elif i == 2: find_data(ask_parametr())
elif i == 3: change_data()
elif i == 4: delete_data()
else: print("Завершение работы")