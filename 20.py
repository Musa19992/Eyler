def fact(a):
    if a == 1 or a == 0:
        return 1
    return fact(a - 1) * a
summa = 0
fact(100)
triant = str(fact(100))
for i in triant:
    summa += int(i)
print(summa)