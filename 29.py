lst = []
for a in range(2, 101):
    for b in range(2, 101):
        lst.append(a**b)
print(len(lst))
lst = set(lst)
print(len(lst))