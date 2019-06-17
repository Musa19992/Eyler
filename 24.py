import itertools
chislo = "0123456789"
chislot = "0123456789"
def swap(a, b):
    t = a
    a = b
    b = t
arr = list(range(1, 10))
def krug(i):
    lst = []
    for i in range(2, 1000000):
        temp = itertools.islice(itertools.permutations(arr), i, None)
        lst.append(temp)

