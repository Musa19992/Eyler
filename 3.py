import time
start=time.time() #Получаем начальное время в секундах от начала времен
l = [0, 1]
i = 1
max = 0
N = int(input("Введите число: "))
while l[i] < N:
    k = 0
    l.append(i)
    if (N % l[i] == 0):
        for j in range (2, l[i] - 1):
            if (l[i] % j == 0):
                k = k + 1
        if (k == 0):
            max = l[i]
    i = i + 1
print("max = %d" %max)
print(time.time()-start) #Получаем конечное время