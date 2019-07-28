import time
start=time.time()
from math import sqrt
lst = []
def pan_chifr(i):
    lst2 = []
    for g in str(i):
        if g not in lst2 and g != '0':
            lst2.append(g)
    if (len(lst2) == len(str(i))):
        return True
    else:
        return False
def deliteli(i):
    for g in range(1, int(sqrt(i)) + 1):
        if (i % g == 0) and (pan_chifr(g) == True) and (pan_chifr(i//g) == True):
            z = str(i) + str(g) + str(i//g)
            p = ''.join(sorted(z))
            if ("123456789" == p):
                lst.append(i)
                break
    return lst
for i in range(1, 10001):
    deliteli(i)
print(sum(lst))
print(time.time()-start)




