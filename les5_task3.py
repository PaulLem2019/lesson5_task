"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("test_file_task3.txt") as fd:
    lines_list = fd.readlines()

# print (lines_list)

# Скорее всего можно через генератор, но пока не сообразил
lines_list1 = []
for item in lines_list:
    lines_list1.append(item.split())

lines_dict = dict(lines_list1)

print (lines_dict)

midle_salary = 0

print ("Сотрудники получающие менее 20 тыс.:")
for item in lines_dict.keys():
    if float(lines_dict.get(item)) <= 20000:
        print (item, float(lines_dict.get(item)))
    midle_salary +=float( lines_dict.get(item))

print("Средняя величина дохода сотрудников: ", midle_salary/len(lines_list))






