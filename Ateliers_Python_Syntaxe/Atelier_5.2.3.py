# -*- coding:utf-8 -*-
# Atelier 5.2.3

# Élimination de doublons
lst = [9, 12, 40, 5, 12, 3, 27, 5, 9, 3, 8, 22, 40, 3, 2, 4, 6, 25]
lst2 = []

for el in lst:
    if el not in lst2:
        lst2.append(el)
lst2.sort()

print("Liste initiale :", lst)
print("Liste traitée :", lst2)