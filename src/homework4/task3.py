"""
Даны два списка чисел.
Посчитайте, сколько различных чисел содержится
одновременно как в первом списке, так и во втором.
"""


list1 = [1, 2, 3, 4, 5, 8, 2]
list2 = [4, 5, 6, 7, 8]
result = set(list1) & set(list2)
print(len(result))

