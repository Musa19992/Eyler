import time
start = time.time()
def prosto(i):
    for g in range(2, int(i**0.5) + 1):
        if i % g == 0:
            return False
    return True
lst = []
for i in range(2, 10000):
    if prosto(i) == True:
        lst.append(i)
maximum = 0
for z in lst:
    chislo = z
    count = 0
    for k in lst[lst.index(z) + 1::]:
            chislo += k
            count += 1
            if prosto(chislo) == True and count > maximum and chislo < 1000000:
                maximum = count
                max_size = chislo
print(max_size)
print(time.time() - start)
