# Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import csv
import json
import os
import pickle


def get_size(path):
    result = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:
            full_path = os.path.join(dirpath, i)
            result += os.path.getsize(full_path)
    return result

def walker(path):
    results = []
    for root, dirs, files in os.walk(path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({'parent_dir': root,
                            'is_file': True,
                            'name': name,
                            'size': os.path.getsize(full_path)})
        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({'parent_dir': root,
                            'is_file': False,
                            'name': name,
                            'size': get_size(full_path)})
        with (open('file.json', 'w') as f1,
              open('file.csv', 'w') as f2,
              open('file.pickle', 'wb') as f3):
            json.dump(results, f1, indent=2)
            writer = csv.DictWriter(f2, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
            pickle.dump(results, f3)

path = 'C:/Users/Diana/Desktop/python_2/seminar7'
walker(path)