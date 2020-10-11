from time import time
slov = {}
i = 1
start = time()
while True:
    z = "".join(sorted(str(i**3)))
    try:
        slov[z][0] += 1
        slov[z].append(i)
        if slov[z][0] == 5:
            k = slov[z].copy()
            break
    except:
        slov[z] = [1,]
        slov[z].append(i)
    i += 1
print(k[1]**3)
print(time() - start)
