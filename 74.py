import time
start=time.time()
lst_fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def suma_fac(i):
    z = 0
    for g in str(i):
        z += lst_fact[int(g)]
    return z
def puti(i):
    lst = [i]
    while 1==1:
        i = suma_fac(i)
        if i not in lst:
            lst.append(i)
        else:
            if len(lst) >= 60:
                return True

            else:
                return False
print(len([1 for i in range(69, 1000000) if puti(i) == True]))
print(time.time()-start)


