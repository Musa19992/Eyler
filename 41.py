import itertools, time
start = time.time()
def prosto(i):
    for g in range(2, int(i**0.5) + 1):
        if i % g == 0:
            return False
    return True
def pan_chifr(i):
    p = ""
    k = ''.join(sorted(str(i)))
    z = [str(i) for i in range(1, len(str(i)) + 1)]
    for t in z:
        p += t
    if k == p:
        return True
    else:
        return False
for i in range(3, 11):
    for t in itertools.permutations(list(range(i))):
        l = int("".join(map(str, t)))
        if pan_chifr(l) == True and prosto(l) == True:
            maximum = l
print(maximum)
print(time.time() - start)



