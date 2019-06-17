import time
start=time.time() #Получаем начальное время в секундах от начала времен
lst = []
i = 3
N = 600851475143
def if_simple(i):
    k = True
    for j in range(2, int(i**0.5) + 1):
        if (i % j == 0):
            k = False
            break
    return k
for i in range(i, int(((N**0.5) + 1)/2)):
    if (N % i == 0):
        t = if_simple(i)
        if (t == True):
            lst.append(i)
        i += 1
print(lst[-1])
print(time.time()-start) #Получаем конечное время