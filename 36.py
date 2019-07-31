import time
start = time.time()
def palind(i):
    if str(i) == str(i)[::-1]:
        return True
    else:
        return False
print(sum([i for i in range(1, 1000000) if palind(i) == True and palind(int(str(bin(i))[2::])) == True]))
print(time.time() - start)