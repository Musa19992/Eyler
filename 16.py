N = 1000

z = 2**N
z = str(z)
summa = 0
for i in range(len(z)):
    summa += int(z[i])
print(summa)