lst = []
for i in range(1, 1000):
    lst.append(i**i)
chislo = str(sum(lst))
print((chislo[-1:-11:-1])[::-1])