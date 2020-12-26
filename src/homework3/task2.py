# 2. List practice

# 1. Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].

list1 = [a + b for a in ['a', 'b'] for b in ['b', 'c', 'd']]
print(list1)

# 2. Используйте на предыдущий список slice
# чтобы получить следующий: ['ab', 'ad', 'bc'].

list2 = list1[0::2]
print(list2)

# 3. Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].

list3 = [a + b for a in ['1', '2', '3', '4'] for b in ['a']]
print(list3)

# 4. Одной строкой удалите элемент
# '2a' из прошлого списка и напечатайте его.
print(list3.pop(1))

# 5. Скопируйте список и добавьте в него элемент '2a' так
# чтобы в исходном списке этого элемента не было.
list4 = list3.copy()
list4.append('2a')
print(list3)
print(list4)