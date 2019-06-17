import time
start=time.time()
sum_kv = 0
kv_sum = 0
lst = []
i = 0
while i <= 100:
    lst.append(i)
    sum_kv += i**2
    i += 1
kv_sum = sum(lst)**2
raz = kv_sum - sum_kv
print("raz = %d" %raz)
print(time.time()-start)