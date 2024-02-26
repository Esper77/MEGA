import csv


def calc_total(data):
    """Расчет общей ценности для каждого привелденного в таблице товара

        Описание переменных:
        data - входной датасет в формате списка списков
        new_data - обработанный датасет в виде списка списков (с добавленным total)

    """
    new_data = [data[0] + ['total']]
    for category, product, date, price, count in data[1:]:
        new_data.append([category, product, date, price, count, int(price[:-2]) * int(count[:-2])])
    return new_data


with open('products.csv', encoding='UTF-8') as file:
    data = [row for row in csv.reader(file, delimiter=";")]


with open('products_new.csv', encoding="UTF-8", mode="w") as file:
    writer = csv.writer(file, delimiter=";")
    new_data = calc_total(data)
    for row in new_data:
        writer.writerow(row)

print(sum(row[5] for row in new_data if row[0] == "Закуски"))
