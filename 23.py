N = 28123
lst2 = []
lst3 = []
lst4 = []
def sumdel(i):
    sum = 1
    for g in range (2, int(i**0.5) + 1):
        if i % g == 0:
            sum += g + (i//g)
    return sum

def proverka(i):
    z = sumdel(i)
    if (i < z):
        lst2.append(i)

for i in range(1, N):
    proverka(i)

for k in range(len(lst2) - 1):
    for t in range(k + 1, len(lst2)):
        lst3.append(lst2[k] + lst2[t])
print(sum([i for i in range(1, N) if i not in lst3]))


