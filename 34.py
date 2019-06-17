import time, math
start=time.time()
def proverka(i):
    summa = 0
    for g in str(i):
        summa += math.factorial(int(g))
    if (summa == i):
        return True
    else:
        return False

t = [i for i in range(3, 10000000) if proverka(i)]
print(sum(t))
print(time.time()-start)