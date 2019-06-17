import time
start=time.time()
N = 1_000_000
i = 1
max_zn = 0
lst1 = []
lst2 = []
def maximum(lst1):
    max_in = 0
    for i in range(len(lst1)):
        if (lst1[i] > max_in):
            max_in = lst1[i]
            max_index = i
    return max_index
def cycle(g):
    k = 0
    while 1 == 1:
        if (g % 2 == 0):
            g = g/2
            k = k + 1
        else:
            g = 3*g + 1
            k = k + 1
        if (g == 1):
            break
    return k + 1

while i < N:
    t = cycle(i)
    if (t > max_zn):
        max_zn = t
        lst1.append(max_zn)
        lst2.append(i)
    i += 1
maxim = maximum(lst1)
print(lst2[maxim])
print(max_zn)
print(time.time()-start)