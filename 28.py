lst = [[]] * 3
for i in range(0,3):
    for j in range(0, 1):
        lst[i].append(j)
n = 3
z = n*n
i = 0
for j in range(0, n - 1):
    lst[i][n - 1 - j] = z
    z = z - 1
print(lst)