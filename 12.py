import time, math
start=time.time()
lst = [1, 3, 6]
def treug(i):
    for g in range(len(lst) - 1, len(lst)):
        lst.append(lst[g] + i)
    return lst
def kol_del(i):
    count = 2
    for g in range(2, int(math.sqrt(i)) + 1):
        if (i % g == 0):
            count = count + 2
    return count
i = 4
while 1==1:
    t = treug(i)[-1]
    if (kol_del(t) > 500):
        print(t)
        break
    i = i + 1
print(time.time()-start)