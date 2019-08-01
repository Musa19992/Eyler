import time
start = time.time()
print(sum([1 for i in range(1, 10) for j in range(1, 22) if len(str((i**j))) == j]))
print(time.time() - start)