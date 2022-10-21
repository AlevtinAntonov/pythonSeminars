# 5) Даны два файла, в каждом из которых находится запись многочлена.
#     Задача - сформировать файл, содержащий сумму многочленов.

with open('file.txt', 'r') as in_file:
    lst = []
    for line in in_file:
        lst.append(line)
print(lst)
lst_res = []
for item in lst:
    item = item.replace('\n', '')
    item = item.replace('=0', '')
    item = item.replace('x^', '*x**')
    lst_res.append(item)
print(lst_res)


