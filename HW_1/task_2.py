# 2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 1 вариант
for x in True, False:
    for y in True, False:
        for z in True, False:
            print('Проверка истинности: ', not (x or y or z) == (not x and not y and not z))
# 2 вариант
res = (not (x or y or z) == (not x and not y and not z) for x in range(2) for y in range(2) for z in range(2))
print(all(res))