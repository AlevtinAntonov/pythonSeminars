# 2. Напишите программу для. проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print('not (', x, 'OR', y, 'OR', z, ') =', not (x or y or z),
                  '==', 'not x', x, 'AND not y', y, 'AND not z', z, '=', not x and not y and not z)
            print('Проверка истинности: ', (not (x or y or z)) == (not x and not y and not z))
