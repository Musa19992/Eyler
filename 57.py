import time
start = time.time()
m = 1
n = 1
count = 0
for i in range(1, 1001):
    chis = m + 2 * n
    znam = m + n
    if (len(str(chis)) > len(str(znam))):
        count += 1
    m = chis
    n = znam
print(count)
print(time.time() - start)