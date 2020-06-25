"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
fd = open ('test_file_task2.txt')
line_file=fd.readlines()
fd.close()
# print (line_file)
print ('Количество строк в файле: ', len(line_file))
for number, item in enumerate (line_file):
    count = 0
    for item1 in item.split():
        count += 1;

    print (f'В строке {number+1}: {item} количество слов: {count} ')
