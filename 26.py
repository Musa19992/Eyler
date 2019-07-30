def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
def funct(i):
    k = 0
    posol = ""
    zet = str(toFixed(1/i, 100))
    for t in zet[2::]:
        posol += t
        if posol == zet[2+len(posol):2 + 2*len(posol):] or zet[2 + k:5 + k:] == zet[2 + 3 + k:5 + 3 + k:]:
            break
        k += 1
    return len(posol)
max = 0
for i in range(1, 999):
    if (funct(i) > max):
        max = i
print(max)