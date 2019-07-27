import time
start=time.time()
lst = [1, 3, 6]
def treug(i):
    for g in range(len(lst) - 1, len(lst)):
        lst.append(lst[g] + i)
for i in range(4, 100):
    treug(i)
f = open("p042.txt", 'r')
tren = f.read()
f.close()
direct = {'A':1, 'B':2, 'C':3, 'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
lst_2 = tren.split(",")
for i in range(len(lst_2)):
    lst_2[i] = lst_2[i][1:-1:]
count = 0
for i in lst_2:
    summa = 0
    for g in i:
        summa += direct[g]
    if summa in lst:
        count += 1
print(count)
print(time.time() - start)
