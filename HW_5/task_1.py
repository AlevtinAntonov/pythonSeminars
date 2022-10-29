# 1. Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

my_text = 'НапившитеБ бА абв1  прбогрАмвму2 пролд  Бав3 текста слова выба4 qwerty содержащие "бва5"'
print(f'Исходный текст: {my_text}')

# out_txt = ' '.join(list(filter(lambda x: ('а' or 'А') and ('б' or 'Б') and ('в' or 'В') not in x, my_text.split())))
# print(f'Текст без слов с буквами абв : {out_txt}')
my_text = my_text.split()
our_list = my_text
print(our_list)
num = []
for i in range(len(our_list)):
    if 'а' in our_list[i].lower():
        if 'б' in our_list[i].lower():
            if 'в' in our_list[i].lower():
                num.append(i)

print(num)
for i in range(len(num)):
    print(i)
    our_list.remove(our_list[num[i]])

print(our_list)

