"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
b_quit = True
with open ("data_user.txt", "w") as fd:
    while b_quit:
        simple_lines = input("Введите строку. Пустая строка - конец ввода ")
        if simple_lines != "":
            simple_lines += '\n'
            fd.write(simple_lines)
        else:
            b_quit = False
