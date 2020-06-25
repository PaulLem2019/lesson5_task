"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
import json

conv_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("test_file_task4.txt") as fd:
    fd_w = open("test_file_task4_out.txt", 'w')
    for line in fd:
        # print (line)
        list_lines = line.split()

        for item in conv_dict.keys():
            if item == list_lines[0]:
                list_lines[0] = conv_dict.get(item)

        list_lines[2] += '\n'
        fd_w.writelines (list_lines)

fd_w.close()