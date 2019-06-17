N = 10000
def deliteli(i):
    lst = []
    for g in range(1, i):
        if (i%g == 0):
            lst.append(g)
    return sum(lst)
def deliteli2(func):
    lst2 = []
    for g in range(1, func):
        if (func%g == 0):
            lst2.append(g)
    return sum(lst2)
def drush(i, N):
    trint = []
    while i < N:
        if(i == deliteli2(deliteli(i)) and (i != deliteli(i))):
            trint.append(i)
        i = i + 1
    return sum(trint)
print(drush(1, N))