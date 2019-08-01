import math, time
start = time.time()
def prosto(i):
    for g in range(2, int(math.sqrt(i)) + 1):
        if i % g == 0:
            return False
    return True
def permuta(i):
    for p in range(len(str(i))):
        if prosto(i) == False:
            return False
        i = int(str(i)[-1] + str(i)[0:-1:])
    return True
print(sum([1 for i in range(2, 1000000) if permuta(i) == True]))
print(time.time() - start)
