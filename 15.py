N = 2
lst = []
summa = 0
k = 0
#for i in range(N + 2):

for i in range(N + 2):
    lst.append([])
    for g in range(N + 2):
        lst[i].append(k)
        k += 1
print(lst)
for i in range(N + 1):
    for g in range(N + 1):
        if (g == N):
            for k in range (N + 1):
                summa += lst[k][g]
        if (i == N):
            for k in range (N + 1):
                summa += lst[i][k]
        while (i*g != N*N):
            summa = str(lst[i][g]) + str(lst)
#print(summa)


