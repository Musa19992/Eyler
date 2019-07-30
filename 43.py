import itertools, time
start = time.time()
lst_1 = [2, 3, 5, 7, 11, 13, 17]
def summ(i):
    k = 0
    for g in range(1, 8):
        if (int(str(i[g]) + str(i[g + 1]) + str(i[g + 2]))) % lst_1[k] != 0:
            return False
        k += 1
    return True
print(sum([int("".join(map(str, i))) for i in itertools.permutations(list(range(10))) if summ(i) == True]))
print(time.time() - start)