import time
start = time.time()
fil = open("p102.txt", "r")
zil = fil.readlines()
lst = []
lst2 = []
for i in zil:
    lst.append(i[:-1:])
for t in lst:
    lst2.append(t.split(","))
for z in range(len(lst2)):
    for p in range(len(lst2[z])):
        lst2[z][p] = int(lst2[z][p])
def reshen(a1, b1, a2, b2, a3, b3):
    return abs((a2-a1) * (b3 - b1) - (a3 - a1)*(b2 - b1))/2
def proverka(a1,b1,a2,b2,a3,b3):
    return (reshen(0,0,a2,b2,a3,b3) + reshen(a1,b1,0,0,a3,b3) + reshen(a1,b1,a2,b2,0,0))
count = 0
for z in range(len(lst2)):
    suma_1 = 0
    suma_2 = 0
    if reshen(lst2[z][0], lst2[z][1], lst2[z][2], lst2[z][3], lst2[z][4], lst2[z][5]) == proverka(lst2[z][0], lst2[z][1], lst2[z][2], lst2[z][3], lst2[z][4], lst2[z][5]):
        count += 1
print(count)
print(time.time() - start)


