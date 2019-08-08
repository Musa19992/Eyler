import time
start = time.time()
hiruzen = {"0":0, "1":1, "2":4, "3":9, "4":16, "5":25, "6":36, "7":49, "8":64, "9":81}
def poluch(i):
    t = 0
    for g in str(i)[::-1]:
        t += hiruzen[g]
    return t
lst = (1, 89)
count = 0
for i in range(2, 10000000):
    z = poluch(i)
    while z not in lst:
        z = poluch(z)
    if z == 89:
        count += 1
    else:
        continue
print(count)
print(time.time() - start)
