import time
start = time.time()
count = 1
z = 2**7830
z_r = int(str(z)[len(str(z)) - 10::])
for i in range(1000):
    count *= z_r
    count = int(str(count)[len(str(count)) - 10::])
otvet = str(((2**457)*28433*(count)) + 1)
print(otvet[len(otvet)-10::])
print(time.time() - start)
