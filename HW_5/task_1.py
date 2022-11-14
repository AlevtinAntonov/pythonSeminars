# 1. Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

my_text = 'НапившитеБ бА АбВ1  прбогрАмвму2 удаляющую из ВИаб3 текста слова, в которых выба4 присутствуют все буквы "бва5"'
print(f'Исходный текст: {my_text}')

our_list = my_text.split()
words_with_letters = []

for i in range(len(our_list)):
    if 'а' in our_list[i].lower():
        if 'б' in our_list[i].lower():
            if 'в' in our_list[i].lower():
                words_with_letters.append(our_list[i])
print()
new_list = ' '.join((filter(lambda s: s not in words_with_letters, my_text.split())))
print(f'Текст без слов с буквами абв или АБВ в любом порядке : \n{new_list}')
