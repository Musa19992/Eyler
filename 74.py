import time
start=time.time()
from math import factorial
def suma_fac(i):
    z = 0
    for i in str(i):
        z +=factorial(int(i))
    return z
def puti(i):
    lst = [i]
    count = 1
    while 1==1:
        i = suma_fac(i)
        if i not in lst:
            count += 1
            lst.append(i)
        else:
            if count >= 60:
                return True
                break
            else:
                return False
                break
otvet = 0
for i in range(69, 1000000):
    if puti(i) == True:
        otvet += 1
print(otvet)
print(time.time()-start)
