import time
import math
start = time.time()
N = 5 * (10**7)
Z = int(math.sqrt(10**8))
R = 10**8
d = {a: 0 for a in range(2, N)}
for i in range(2, N//2):
    for g in range(i * 2, N, i):
        d[g] += 1
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
k = 0
for i in range(len(list_d)):
    if list_d[i][1] == 1 or list_d[i][0] > Z:
        break
    else:
        for g in range(i, len(list_d)):
            if list_d[g][1] == 1 or list_d[i][0] * list_d[g][0] > R:
                break
            else:
                k += 1
print(k)
print(time.time() - start)