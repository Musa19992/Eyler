import math
N = 28124
lst2 = []
lst3 = []
def sumdel(i):
    sum = 1
    for g in range (2, int(i**0.5) + 1):
        if i % g == 0:
            sum += g + (i/g)
        if i / g == math.sqrt(i):
            sum = sum - g
    return sum

def proverka(i):
    z = sumdel(i)
    if (i < z):
        lst2.append(i)

for i in range(1, N):
    proverka(i)
print(lst2)
for i in range(len(lst2)):
    for g in range(i, len(lst2)):
        lst3.append(lst2[i] + lst2[g])
lst3 = sorted(set(lst3))
print(sum([t for t in range(N) if t not in lst3]))


