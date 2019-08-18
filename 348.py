from math import sqrt
import time
start = time.time()
def palind(i):
    palindrom = str(i)
    return palindrom == palindrom[::-1]
def functi(i):
    count = 0
    p = 2
    for z in range(int(i**(1/3)) - 1, int(i**(1/3))//2, -1):
        tent = i - (int(i**(1/3)) - 1 - z + 2)**3
        kent = i - z**3
        if sqrt(kent) == int(sqrt(kent)):
            count += 1
        if sqrt(tent) == int(sqrt(tent)):
            count += 1
        if count > 4:
            break
    if count == 4:
        return True
    else:
        return False
k = 1
otvet = 0
counter = 0
while True:
    lst = []
    sven = str(k)
    sveni = str(k)[:-1:]
    a = int(sven + sven[::-1])
    for m in range(0, 10):
        b = int(sven + str(m) + sven[::-1])
        if functi(b) == True:
            otvet += b
            counter += 1
            break
    if functi(a) == True:
        otvet += a
        counter += 1
    if counter == 5:
        break
    k += 1
print(otvet)
print(time.time() - start)



