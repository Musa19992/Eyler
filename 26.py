from operator import index
max = 0
lst1 = []
lst2 = []
for i in range(2, 1000):
    k = []
    t = float(1/i)
    count = ""
    for g in range(2, len(str(t)) - 1):
        if (str(t)[g] != str(t)[g + 1]):
            count += str(t)[g]
        elif (str(t)[g] == str(t)[g + 1]):
            if (len(count) > max):
                max = len(count)
                indexav = i
                lst1.append(max)
                lst2.append(indexav)
            count = ""
maxim = 0
print(lst1)
print(lst2)
for i in range(len(lst1)):
    if lst1[i] > maxim:
        maxim = lst1[i]
        kint = i
print(lst2[kint])
