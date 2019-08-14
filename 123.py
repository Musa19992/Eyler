from math import sqrt
lim = 10**10
lst = [5]
def prosto(z):
    for t in range(2, int(sqrt(z)) + 1):
        if z % t == 0:
            return False
    return True
n = 3
i = 5
while True:
    if n * lst[-1] * 2 > lim:
        break
    if prosto(i) == True:
        lst.append(i)
        n += 1
    i += 2
print(n)