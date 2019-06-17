import time
start=time.time()
max = 0
sum = 0
lst = []
lst2 = []
z = 0
for i in range(100, 1000):
    lst.append(i)
    n = 0
    for j in range(100, 1000):
        k = 0
        lst2.append(j)
        sum = lst[z] * lst2[n]
        i += 1
        j += 1
        sum = str(sum)
        dlina = len(sum)
        for g in range(0, len(sum) - 1):
            if (sum[g] != sum[len(sum) - 1 - g]):
                k = k + 1
        sum = int(sum)
        if (k == 0 and sum > max):
            max = sum
        n = n + 1
    z = z + 1
print("max = %d" %max)
print(time.time()-start)