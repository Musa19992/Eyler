import time
start = time.time()
class Zadanie:
    lst = []
    def __init__(self, z, k):
        self.lst = [1]
        self.k = k
        self.z = z
        for i in range(1000):
            self.lst.append(self.lst[i] + k)
            k += z
            if len(str(self.lst[-1])) > 4:
                self.lst = self.lst[:-1:]
                for i in self.lst:
                    if len(str(i)) == 4:
                        self.lst = self.lst[self.lst.index(i)::]
                        break
                break
def pr(i, g):
    if str(i)[:2:] == str(g)[2::]:
        return True
    else:
        return False

dva = Zadanie(2, 3)
tri = Zadanie(1, 2)
five = Zadanie(3, 4)
six = Zadanie(4, 5)
seven = Zadanie(5, 6)
vosem = Zadanie(6, 7)
lostit = [dva.lst, tri.lst, five.lst, six.lst, seven.lst, vosem.lst]
listik = sorted(set(dva.lst + tri.lst + five.lst + six.lst + seven.lst + vosem.lst))
def prov(a,b,c,d,e,f,lst):
    for i in range(len(lst)):
        if a in lst[i]:
            grin = lst[:i:] + lst[i + 1::]
            for p in range(len(grin)):
                if b in grin[p]:
                    simka = grin[:p:] + grin[p + 1::]
                    for k in range(len(simka)):
                        if c in simka[k]:
                            trinka = simka[:k:] + simka[k + 1::]
                            for rin in range(len(trinka)):
                                if d in trinka[rin]:
                                    kirka = trinka[:rin:] + trinka[rin + 1::]
                                    for ton in range(len(kirka)):
                                        if e in kirka[ton]:
                                            obito = kirka[:ton:] + kirka[ton + 1::]
                                            for kint in range(len(obito)):
                                                if f in obito[kint]:
                                                    return True
    return False
count = 0
otvet = []
for i in listik:
    for g in listik:
        if pr(g, i) == True and g != i:
            for h in listik:
                if pr(h, g) == True and h != g:
                    for t in listik:
                        if pr(t, h) == True and t != h:
                            for m in listik:
                                if pr(m, t) == True and m!= t:
                                    for le in listik:
                                        if pr(le, m) == True and le != m and pr(i, le):
                                            if prov(i, g, h, t, m, le, lostit):
                                                otvet.append(eval(str(i) + "+" + str(g) + "+" + str(h) + "+" + str(t) + "+" + str(m) + "+" + str(le)))
print(str(set(otvet))[1:-1:])
print(time.time() - start)