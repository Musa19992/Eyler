import time
start=time.time()
lst = [2]
i = 2
def if_simple(i):
    k = True
    for j in range(2, int(i**0.5) + 1):
        if (i % j == 0):
            k = False
            break
    return k
while 1 == 1:
    i += 1
    t = if_simple(i)
    if (t == True):
        lst.append(i)
    if (len(lst) == 10001):
        break
print("prosto = %d" %lst[10000])
print(time.time()-start)



