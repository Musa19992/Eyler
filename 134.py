from math import sqrt
import time
start = time.time()
lim = 1000000
lst = []
def prosto(i):
    for t in range(2, int(sqrt(i)) + 1):
        if i % t == 0:
            return False
    return True
kura = 5
while True:
    if kura > lim and prosto(kura) == True:
        lst.append(kura)
        break
    elif prosto(kura) == True:
        lst.append(kura)
    kura += 2
def functi2(a, b):
    q = 1
    while q < 10:
        if str(q*int(str(b)[-1]))[-1] == str(a)[-1]:
            break
        else:
            q += 1
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
    while q < 100:
        if str(q*int(str(b)[-2::]))[-2::] == str(a)[-2::]:
            break
        else:
            q += 10
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
    while q < 1000:
        if str(q * int(str(b)[-3::]))[-3::] == str(a)[-3::]:
            break
        else:
            q += 100
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
    while q < 10000:
        if str(q * int(str(b)[-4::]))[-4::] == str(a)[-4::]:
            break
        else:
            q += 1000
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
    while q < 100000:
        if str(q * int(str(b)[-5::]))[-5::] == str(a)[-5::]:
            break
        else:
            q += 10000
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
    while q < 1000000:
        if str(q * int(str(b)[-6::]))[-6::] == str(a)[-6::]:
            break
        else:
            q += 100000
    if str(q * b)[-len(str(a))::] == str(a):
        return q * b
print(sum([functi2(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]))
print(time.time() - start)#8 sec