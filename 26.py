from math import sqrt
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
def funct(i):
    k = 0
    posol = ""
    zet = str(toFixed(1/i, 100))
    for t in zet[3::]:
        posol += t
        if posol == zet[3 + len(posol):3 + 2*len(posol):] or zet[5:5 + 2:] == zet[7:7 + 2:]:
            break
        k += 1
    return len(posol)
max = 0
otvet = 0
for i in range(1, 999):
    if (funct(i) > max):
        otvet = i
        max = funct(i)
print(otvet)