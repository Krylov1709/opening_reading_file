import os

current_directory = (os.listdir('C:\Моя папка\Нетология\Домашнее задание\Открытие и чтение файла\Task 3'))

# Читаем все текстовые файлы в дериктории
def reading_file(current_directory: list) -> dict:
    file_txt = {}
    for file in current_directory:
        if '.txt' in file and file != 'total.txt': 
            with open(file, encoding='utf-8') as open_file:
                file_txt[file] = []    
                for line in open_file:           
                    file_txt[file].append(line.strip())                  
    return file_txt

# Сортируем словарь по количеству строк в файле
file_txt = reading_file(current_directory)
new_dict = {}
for key, values in file_txt.items():
   new_dict[key] = len(values)
sorted_values = sorted(new_dict.values())
sorted_dict = {}
for i in sorted_values:
    for key in new_dict.keys():
        if new_dict[key] == i:
            sorted_dict[key] = file_txt[key]
print(sorted_dict)

# Записываем данные в файл
def record_file(file_name, mod, file_for_record):
    with open(file_name,mod) as file:
        for key in file_for_record:
            file.write(f'{key}\n')
            file.write(f'{len(file_for_record[key])}\n')
            for i in file_for_record[key]:
                file.write(f'{i}\n')

record_file('total.txt', 'w', sorted_dict)