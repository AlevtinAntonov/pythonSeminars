# 5) Даны два файла, в каждом из которых находится запись многочлена.
#     Задача - сформировать файл, содержащий сумму многочленов.

with open('file.txt', 'r', encoding='utf8') as in_file:
    # while True:
    #     line = in_file.readline()
    #     if not line:
    #         break
    #     print(line.strip())
    lst = []
    for line in in_file:
        lst.append(line)
print(lst)
new_lst = []
for i in range(len(lst)):
    lst[i].replace(' = 0', '')
    lst[i] = lst[i].split(' + ')
    new_lst.append(lst[i])
    for i in range(len(new_lst[i])):
        if new_lst[i] == 'x':
            new_lst[i] = '1'

    print(new_lst)





