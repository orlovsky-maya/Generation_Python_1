n = int(input())
l_1 = []
for l in range(n):
    l_2 = [int(i) for i in input().split()]
    def quick_merge(list1, list2):
        result = []
        p1 = 0
        p2 = 0
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1

        if p1 < len(list1):
            result += list1[p1:]
        if p2 < len(list2):
            result += list2[p2:]

        return result
    l_1 = quick_merge(l_1, l_2)
print(*l_1)


# list3 = quick_merge(l_1, l_2)
# print(list3)





