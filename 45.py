import time
start = time.time()
pyt = [1]
shest = [1]
treug = [1]
p_z = 3
p_sh = 4
def treugi(i):
    treug.append(treug[i - 1] + 1 + i)
    return treug[-1]
def pyti(i, pyti_z):
    pyt.append(pyt[i - 1] + i + pyti_z)
def shesti(i, pyti_shesti):
    shest.append(shest[i - 1] + i + pyti_shesti)
i = 1
count = 0
while 1 == 1:
    z = treugi(i)
    pyti(i, p_z)
    shesti(i, p_sh)
    p_z += 2
    p_sh += 3
    i += 1
    if z in shest and z in pyt:
        count += 1
    if count == 2:
        print(z)
        break
print(time.time() - start)