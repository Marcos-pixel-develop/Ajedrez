import sys
from decimal import *
n = input()

lista_shift = list(map(lambda x:int(x), list(n.strip())))
r = [0]
k = len(n)
if n.count("0")==k:
    r.append(-1)


if n.count("1")!=k and n.count("0")!=k:

    for j in range(k):

        acum = 0
        count = 0
        y = lista_shift.copy()
        for i in range(k):
            acum += lista_shift[i]*pow(2,k-i-1)
            lista_shift[i] = y[i-1]
if -1 in r:
    print(-1)
else:
    print(max(r))


