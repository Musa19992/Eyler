import time
start=time.time()
lst = [2]
i = 2
lst1 = [1]
lst2 = [2]
def if_simple(g):
    k = True
    for j in range(2, int(g**0.5) + 1):
        if (g % j == 0):
            k = False
            break
    return k
def list_prime(lit, g):
    for i in range(g, lit):
        t = if_simple(i)
        if (t == True):
            lst.append(i)
    return sum(lst)
summa = list_prime(2000000, i)
print("sum = %d" %sum(lst))
print(time.time()-start)
