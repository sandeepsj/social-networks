import networkx as nx
import random
import numpy
import matplotlib.pyplot as plt
def add_nodes(n):
    G=nx.Graph()
    G.add_nodes_from(range(n))
    return G
def add_random_edge(G):
    v1=random.choice(list(G.nodes()))
    v2=random.choice(list(G.nodes()))
    if(v1!=v2):
        G.add_edge(v1,v2)
    return G
def add_till_connectivity(G):
    while (nx.is_connected(G)==False):
        G=add_random_edge(G)
    return G
def create_instance(n):
    G=add_nodes(n)
    G=add_till_connectivity(G)
    return G.number_of_edges()
def create_avg_instance(n):
    list1=[]
    for i in range(0,100):
        list1.append(create_instance(n))
    return numpy.average(list1)
def plot_connectivity():
    x=[]
    y=[]
    i=10
    while(i<=400):
        x.append(i)
        y.append(create_avg_instance(i))
        i=i+10
    plt.xlabel('Number of nodes')
    plt.ylabel('number of edges required to connect the graph')
    plt.plot(x,y)
    x1=[]
    y1=[]
    i=10
    while(i<=400):
        x1.append(i)
        y1.append(i*numpy.log(i))
        i=i+10
    plt.plot(x1,y1)
    plt.show()
