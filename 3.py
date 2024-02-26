import csv
with open('products.csv', encoding='UTF-8') as file:
    data = [row for row in csv.reader(file, delimiter=";")]

hash_table = {}
for row in data[1:]:
    if row[0] not in hash_table.keys():  # Создание или добавление к уже существующим значения кол-ва товаров
        hash_table[row[0]] = {row[1]: int(row[4][:-2])}
    else:
        if row[1] not in hash_table[row[0]].keys():
            hash_table[row[0]] = {row[1]: int(row[4][:-2])}
        else:
            hash_table[row[0]][row[1]] += int(row[4][:-2])


query = ""

while query != "молоко":
    query = input()
    if query in hash_table.keys():
        vals = list(hash_table[query].items())
        vals.sort(key=lambda a: a[1])

        print(f"В категории: {query} товар: {vals[0][0]} был куплен {vals[0][1]} раз")
    else:
        print("Такой категории не существует в нашей БД")
