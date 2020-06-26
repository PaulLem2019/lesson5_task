"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open("test_file_task7.txt") as fd:
    lines_list = fd.readlines()

lines_list1 = []
for item in lines_list:
    lines_list1.append(item.split())

print (lines_list1)
lines_dict = dict()
average = dict()
sum_average = 0
for item in lines_list1:
    name = item[0]
    profit = item[2]
    sum_average = float(item[2]) - float(item[3])
    lines_dict[name] = profit

average['average_profit'] = sum_average / len (lines_list1)

firm_data = [lines_dict, average]

with open('statist.txt', 'w') as fd:
    print ("Запись в файл в формате json:")
    print (firm_data)
    json.dump(firm_data, fd)

with open('statist.txt') as fd:
    print ("Чтение из файла формата json:")
    read_data = json.load(fd)
    print (read_data)
    print (type(read_data))
