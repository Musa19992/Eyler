def stepen(i):
    summa = 0
    for g in str(i):
        summa += int(g)**5
    if (summa == i):
        return True
    else:
        return False
lst = []
for i in range(2, 1000000):
    if (stepen(i) == True):
        lst.append(i)
print(sum(lst))