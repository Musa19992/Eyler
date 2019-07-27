import time
start=time.time()
from math import sqrt
def perim(t):
    count = 0
    for a in range(1, int(t/4) + 1):
        for b in range(a + 1, int((t - a)/2) + 1):
            c = sqrt(a**2 + b**2)
            if (a + b + c == t):
                count += 1
    return count
maxim = 0
for i in range(10,1001):
    k = perim(i)
    if k > maxim:
        maxim = k
        trin = i
print(trin)
print(time.time()-start)