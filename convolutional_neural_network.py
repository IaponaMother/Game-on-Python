import random
list1, list2, result = [], [], []

for i in range(4):
    list1.append([])
    for j in range(4):
        list1[i].append(random.randint(0, 10))
for i in list1:
    print(i)


for i in range(4):
    list2.append(random.randint(1, 3))


for i in range(4):
    a = 0
    for j in range(4):
        a += list1[i][j] * list2[i]
    result.append(a)
print(result)