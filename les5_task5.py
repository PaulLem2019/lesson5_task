"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

with open ('gen_file.txt', 'w+') as file_number:
    for numb in range(100):
        file_number.write(str(random.randint(0, 100)))
        file_number.write(" ")

    file_number.seek(0)

    number_list = 0
    for line in file_number:
        number_list = line.split()

    sum = 0
    for iter in number_list:
        sum += int(iter)

    print ('Сумма чисел в файле = ', sum)