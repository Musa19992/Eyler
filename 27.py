def prosto(i):
    z = True
    for g in range(2, int(abs(i)**0.5) + 1):
        if (i%g == 0):
            z = False
            break
    return z
count = 0
max = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        for n in range(0, 1000):
            if (prosto(n**2 + a*n + b) == True):
                count += 1
            else:
                if (count > max):
                    max = count
                    umnosh = a*b
                count = 0
                break
print(umnosh)




