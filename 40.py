import time
start = time.time()
count = ""
t = 1
otvet = 1
for i in range(1, 1000000):
    count += str(i)
    if (i % t == 0):
        otvet *= int(count[i - 1])
        t *= 10
    if len(count) > 1000000:
        break
print(otvet)
print(time.time() - start)