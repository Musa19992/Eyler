N = 28123
lst2 = []
lst3 = []
def sumdel(i):
    lst = []
    for g in range(1, i):
        if (i % g == 0):
            lst.append(i)
    return sum(lst)

def proverka(i):
    if (i < sumdel(i)):
        lst2.append(i)
def summa(N):
    for i in range(1, N):
        proverka(i)
    for g in lst2:
        for k in lst2:
            summator = 0
            summator = g + k
            if summator not in lst3:
                lst3.append(summator)
summa(N)

res = 0
for i in range(1, N):
    if i in lst3:
        res += i
print(res)


"""def compute():
    LIMIT = 29
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

    expressible = [False] * LIMIT
    for i in abundantnums:
        for j in abundantnums:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break

    ans = sum(i for (i, x) in enumerate(expressible) if not x)
    return str(ans)


if __name__ == "__main__":
    print(compute())"""


