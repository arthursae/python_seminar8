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


file_name = 'data.txt'

new_entry = 'Фамилия5 Имя5 Отчество5,+555555555555'
# add_data(file_name, new_entry)
# found_data = find_data(file_name, ' мил ')
# print(f'Найдено: {len(found_data)}')
# print(*output_data(file_name, found_data), sep='\n')
# update_data(file_name, 'Фамилия99 Имя99 Отчество99,+999999999999', 2)
# delete_data(file_name, 3)
print(*get_entries(file_name), sep='\n')
