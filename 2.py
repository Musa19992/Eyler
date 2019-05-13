import time
start=time.time() #Получаем начальное время в секундах от начала времен
l=[1,2]
i = 1
result = 0
while l[i] < 4000000:
    i = i + 1
    l.append(l[i-1]+l[i-2])
    if (l[i] % 2 == 0):
        result = result + l[i]
print("sum = %d" %result)
print(time.time()-start) #Получаем конечное время
