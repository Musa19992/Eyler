import time
start = time.time()
def funct(u):
	return set([int(i) for i in str(u)])
	
def sravn(a, b, c, d, e):
	if a == b == c == d == e:
		return True
x = 10
while sravn(funct(2 * x), funct(3 * x), funct(4 * x), funct(5 * x), funct(6 * x)) != True:
	x += 1
print(time.time() - start)
print(x)