import time
start=time.time()
lst = [11, 13, 14, 15, 16, 17, 18, 19, 20]
min = 0
number = 0
while 1 == 1:
    number += 20
    k = 0
    for i in range (0, 8):
        if(number % lst[i] != 0):
            break
        else:
            k += 1
    if (k == 8):
        min = number
        break
print("min = %d" %min)
print(time.time()-start)

