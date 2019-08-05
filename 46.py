from math import sqrt
import time
start = time.time()
def prosto(i):
    for g in range(2, int(sqrt(i)) + 1):
        if i % g == 0:
            return False
    return True
def proverka(i):
    k = 1
    while i >= 2 * (k**2):
        if prosto((i - 2 * (k**2))) == True:
            return True
        k += 1
    return False
i = 33
count = 0
while True:
    if prosto(i) == False and proverka(i) == False:
        print(i)
        break
    i += 2
print(time.time() - start)