import time
start=time.time() #Получаем начальное время в секундах от начала времен
chislo = 1000
sum = 0
for i in range(1, 1000):
    if(i % 3 == 0) or (i % 5 == 0):
        sum = sum + i
print("sum = %d" %int(sum))
print(time.time()-start) #Получаем конечное время
