n = 1000
lst2 = [1, 1, 2, 3]
def fibonachi(i):
    for g in range(len(lst2) - 1, i - 1):
        lst2.append(lst2[g] + lst2[g - 1])
    return (lst2)

i = 5
lst = []
while 1 == 1:
    if (len(str(fibonachi(i)[-1])) == n - 1):
        lst.append(i)
    if (len(str(fibonachi(i)[-1])) > n - 1):
        break
    i += 1
print(lst[-1] + 1)