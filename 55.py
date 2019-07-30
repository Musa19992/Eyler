import time
start = time.time()
def Lich(i):
    for g in range(50):
        i = (i + int(str(i)[::-1]))
        if palind(i) == True:
            return True
    return False

def palind(i):
    if str(i) == str(i)[::-1]:
        return True
    else:
        return False
print(sum([1 for i in range(1, 10000) if Lich(i) == False]))
print(time.time() - start)