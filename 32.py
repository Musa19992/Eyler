import math
lst_z = []
def pan_chifr(i):
    lst = []
    for g in str(i):
        if g not in lst and g != '0':
            lst.append(g)
    if (len(lst) == len(str(i))):
        return True
    else:
        return False
def deliteli(i):
    lst = []
    for g in range(37, int(i**0.5) + 1):
        if (i % g == 0):
            lst.append(g)
            lst.append(i//g)
            break
    return lst
def uslovie(kent, z):
    for i in str(kent):
        if i in str(z):
            return False
            break
    return True
def delitel(i):
    t = deliteli(i)
    if (pan_chifr(i) == True):
        if (len(t) > 1):
            stroka = str(i) + str(t[0]) + str(t[1])
            if "".join(sorted(stroka)) == "123456789":
                lst_z.append(i)
                print(i)
for i in range(1, 10001):
    delitel(i)
print(sum(lst_z))


"""def compute():
    # For contradiction suppose a candidate (x, y, z) has z >= 10000.
    # Then x*y consumes at least 5 digits. With the 4 (or fewer) remaining digits, even the
    # upper bound of x=99 and y=99 produces a product of x*y < 10000, which is unequal to z.
    # Therefore we need the product z < 10000 to be able to find possible x and y values.
    for i in range(1, 10000):
        if has_pandigital_product(i):
            print(i)


def has_pandigital_product(n):
    # Find and examine all factors of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


if __name__ == "__main__":
    print(compute())"""


