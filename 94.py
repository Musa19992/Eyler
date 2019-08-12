from math import sqrt
import time
start = time.time()
def proverka(a, b):
    z = sqrt(a**2 - (b/2)**2)
    if b % 2 != 0 and z % 2 != 0:
        return False
    if int(z) != z:
        return False
    return True
n = 1000000000
otvet = 0
i = 3
while i < n//3:
    t = i - 1
    while t < i + 2:
        ll = i * 2 + t
        if ll > n:
            break
        elif proverka(i, t) == False and t == i + 1:
            i, t = t, i
        elif proverka(i, t) == True:
            otvet += ll
            break
        else:
            t += 2
    i = (i * 3) + i//2
print(otvet)
print(time.time() - start)
