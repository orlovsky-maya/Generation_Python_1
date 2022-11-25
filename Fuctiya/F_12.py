# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    sortirov_list_1 = []
    for i in range(len(list1)):
        minimum = min(list1)
        sortirov_list_1.append(minimum)
        del list1[list1.index(minimum)]
    return sortirov_list_1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))