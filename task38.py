# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных


def get_entries(file_name: str) -> [str]:
    with open(file_name, 'r', encoding="utf-8") as file:
        file_source = file.read()
        entries = list(file_source.split('\n'))
        if entries[-1] == '':
            entries.pop()
        return entries


def save_data(file_name: str, file_source: str):
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(file_source)


def add_data(file_name: str, data: str):
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(f'{data}\n')
        print(f'Данные добавлены')


def output_data(file_name: str, rows: [int]) -> [str]:
    output_entries = list()
    if len(rows) > 0:
        entries = get_entries(file_name)
        output_entries = [entries[i] for i in rows]
    return output_entries


def find_data(file_name: str, search_query: str) -> [int]:
    found_items = list()
    search_query = search_query.strip()
    if len(search_query) > 0:
        entries = get_entries(file_name)
        entries = list(map(lambda x: x.split(','), entries))
        for row, entry in enumerate(entries):
            if any(search_query.lower() in str(item).lower() for item in entry):
                found_items.append(row)
    return found_items


def update_data(file_name: str, new_entry: str, at_row: int):
    entries = get_entries(file_name)
    if 0 <= at_row < len(entries):
        entries[at_row] = new_entry
        entries_formated = str()
        for entry in entries:
            entries_formated += entry + '\n'
        save_data(file_name, entries_formated)
        print(f'Данные в строке {at_row} обновлены')
    else:
        print(f'Нет данных в строке {at_row}')


def delete_data(file_name: str, at_row: int) -> [str]:
    entries = get_entries(file_name)
    if 0 <= at_row < len(entries):
        entries.pop(at_row)
        entries_formated = ''.join([i + '\n' for i in entries])
        save_data(file_name, entries_formated)
        print(f'Данные в строке {at_row} удалены')
    else:
        print(f'Нет данных в строке {at_row}')

def display_menu():
    print('0 - Отобразить список всех записей')
    print('1 - Поиск по ключевому слову')
    print('2 - Добавить новую запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    print('5 - Выйти')


def switchboard():
    mode = int(input('Введите опцию 0-5: '))
    while True:
        match mode:
            case 0:
                print(*get_entries(file_name), sep='\n')
                return switchboard()
            case 1:
                keyword = input('Введите ключевое слово для поиска: ')
                found_data = find_data(file_name, keyword)
                print(f'Найдено: {len(found_data)}')
                print(*output_data(file_name, found_data), sep='\n')
                return switchboard()
            case 2:
                new_entry = input('Введите ФИО, телефон: ')
                add_data(file_name, new_entry)
                return switchboard()
            case 3:
                entry_id = int(input('Введите номер записи: '))
                update_entry = input('Введите новые данные ФИО, телефон: ')
                update_data(file_name, update_entry, entry_id)
                return switchboard()
            case 4:
                delete_id = int(input('Введите номер записи которую нужно удалить: '))
                delete_data(file_name, delete_id)
                return switchboard()
            case 5:
                return False
            case _:
                return False

file_name = 'data.txt'
display_menu()
switchboard()
