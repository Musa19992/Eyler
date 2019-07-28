import time
start = time.time()
def functt(i, t):
    for q in str(i):
        if q in str(t):
            new_i = str(i).replace(str(q), "")
            new_t = str(t).replace(str(q), "")
            if new_i == "":
                new_i = str(1)
            if new_t == "":
                new_t = str(999)
            if (i/t) == (int(new_i)/int(new_t)):
                return True
            else:
                return False
otvet = 1
otvet2 = 1
for i in range(11, 100):
    for g in range(11, 100):
        if (i % 10 != 0) and (g % 10 != 0) and (i != g) and (i > g):
            if functt(i, g) == True:
                otvet *= g
                otvet2 *= i
print(otvet2//otvet)
print(time.time() - start)

