import math
lst_z = []
def pan_chifr(i):
    lst = []
    for g in str(i):
        if g not in lst and g != '0':
            lst.append(g)
    if (len(lst) == len(str(i))):
        return True
    else:
        return False
def deliteli(i):
    lst = []
    for g in range(37, int(i**0.5) + 1):
        if (i % g == 0):
            lst.append(g)
            lst.append(i//g)
            break
    return lst
def uslovie(kent, z):
    for i in str(kent):
        if i in str(z):
            return False
            break
    return True
def delitel(i):
    t = deliteli(i)
    if (pan_chifr(i) == True):
        if (len(t) > 1):
            stroka = str(i) + str(t[0]) + str(t[1])
            if "".join(sorted(stroka)) == "123456789":
                lst_z.append(i)
                print(i)
for i in range(1, 10001):
    delitel(i)
print(sum(lst_z))



