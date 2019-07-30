import itertools
kent = ""
count = 0
for i in itertools.permutations(list(range(10))):
    if count == 999999:
        for t in i:
            kent += str(t)
        break
    count += 1
print(kent)
