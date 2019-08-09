import time
start = time.time()
lst = []
for i in range(1, 12001):
    for t in range(1, 12001):
        if t >= i:
            break
        if t/i > 1/3 and t/i < 1/2:
            lst.append(t/i)
print(len(set(lst)))
print(time.time() - start)