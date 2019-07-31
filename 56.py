import time
start = time.time()
def summa(i):
    return(sum([int(g) for g in str(i)]))
maximum = 0
for t in range(1, 100):
    for i in range(1, 100):
        r = summa(t**i)
        if r > maximum:
            maximum = r
print(maximum)
print(time.time() - start)