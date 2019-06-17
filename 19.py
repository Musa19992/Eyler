a = "001000001110001000"
a1 = sorted(a.split("1"))[-1]
s1 = a.find(a1)
final_spisok = (a[s1 - 1 : s1 + len(a1) + 1])
print(final_spisok)