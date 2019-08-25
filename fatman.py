import networkx as nx
import matplotlib.pyplot as plt
import random
import math

def create_graph(n):
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    return G
def visualize(G,labeldict,nsize,color):
    nx.draw(G,labels = labeldict,node_size = nsize,node_color = color)
    plt.show()
def assign_bmi(G):
    for each in G.nodes():
        G.node[each]['name'] = random.randint(15,40)
        G.node[each]['type'] = 'person'
def get_labels(G):
    dict1 = {}
    for each in G.nodes():
        dict1[each] = G.node[each]['name']
    return dict1
def get_size(G):
    array1 = []
    for each in G.nodes():
        if G.node[each]['type'] == 'person':
            array1.append(G.node[each]['name']*20)
        else:
            array1.append(1000)
    return array1
def add_foci_nodes(G):
    n = G.number_of_nodes()
    i = n+1
    foci_nodes = ['gym', 'eatout', 'movie_club', 'karate_club', 'yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G.node[i]['name'] = foci_nodes[j]
        G.node[i]['type'] = 'foci'
        i+=1
def get_color(G):
    c = []
    for each in G.nodes():
        if G.node[each]['type'] == 'person':
            if G.node[each]['name'] == 15:
                c.append('green')
            elif G.node[each]['name'] == 40:
                c.append('yellow')
            else:
                c.append('blue')
        else:
            c.append('red')
    return c
def get_foci_nodes():
    f = []
    for each in G.nodes():
        if G.node[each]['type'] == 'foci':
            f.append(each)
    return f
def get_person_nodes():
    p = []
    for each in G.nodes():
        if G.node[each]['type'] == 'person':
            p.append(each)
    return p
def add_foci_edges(G):
    foci_nodes = get_foci_nodes()
    person_nodes = get_person_nodes()
    for each in person_nodes:
        r = random.choice(foci_nodes)
        G.add_edge(each,r)
def homophily(G):
    pnodes = get_person_nodes()
    for u in pnodes:
        for v in pnodes:
            if u!=v:
                diff = abs(G.node[u]['name'] - G.node[v]['name'])
                p = 1.0/(diff+1000)
                r=random.uniform(0,1)
                if (r<p):
                    G.add_edge(u,v)
def cmn(u,v,G):
    nu = set(G.neighbors(u))
    nv = set(G.neighbors(v))
    return len(nu & nv)
def closure(G):
    array1 = []
    for u in G.nodes():
        for v in G.nodes():
            if v!=u and (G.node[u]['type']=='person' or G.node[v]['type']=='person'):
                k=cmn(u,v,G)
                p=1-math.pow(1-0.01,k)
                tmp = []
                tmp.append(u)
                tmp.append(v)
                tmp.append(p)
                array1.append(tmp)
    for each in array1:
        u = each[0]
        v = each[1]
        p = each[2]
        r = random.uniform(0,1)
        if(r<p):
            G.add_edge(u,v)
G = create_graph(100)
assign_bmi(G)
add_foci_nodes(G)
labeldict = get_labels(G)
arraysize = get_size(G)
colorarray = get_color(G)
add_foci_edges(G)

visualize(G,labeldict,arraysize,colorarray)
homophily(G)
visualize(G,labeldict,arraysize,colorarray)
while(1):
    closure(G)
    visualize(G,labeldict,arraysize,colorarray)
