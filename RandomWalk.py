import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy

def walk(n, p):
    start = random.randint(0, n-1)
    G = nx.erdos_renyi_graph(n,p)
    S = set([])
    v = start
    count = 0
    while(len(S)<n):
        global Nbr
        Nbr = list(G.neighbors(v))
        v = random.choice(Nbr)
        S.add(v)
        count += 1
    return count

l=[]
for i in range(20, 300):
    z=[]
    for j in range(10):
        z.append(walk(i, 0.3))
    l.append(numpy.average(z))
    print (i, "--->", numpy.average(z))
plt.plot(l)
plt.show()
