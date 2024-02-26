import csv
with open('products.csv', encoding='UTF-8') as file:
    data = [row for row in csv.reader(file, delimiter=";")]

hash_table = {}
for row in data[1:]:
    if row[1] not in hash_table.keys():  # Создание или добавление к уже существующим значения кол-ва товаров
        hash_table[row[1]] = int(row[4][:-2])
    else:
        hash_table[row[1]] += int(row[4][:-2])
for item in hash_table.items():
    print(f"{item[0]}, {item[1]}")