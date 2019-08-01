from math import sqrt
import time
start = time.time()
lst = []
def prosto(i):
    for g in range(2, int(i**0.5) + 1):
        if i % g == 0:
            return False
    return True
for i in range(2, int(sqrt(50000000)) + 1):
    if prosto(i) == True:
        lst.append(i)
lst_2 = []
def summa(i):
    count = 0
    for a in lst:
        if a**2 > i:
            break
        for b in lst:
            if a**2 + b**3 > i:
               break
            for c in lst:
                if a**2 + b**3 + c**4 > i:
                    break
                else:
                    lst_2.append(a**2 + b**3 + c**4)
    return lst_2
print(len(set(summa(50000000))))
print(time.time() - start)