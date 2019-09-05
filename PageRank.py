'''
Create take a directed graph with 'n' nodes
Assigning 100 points to each node
keep distributing points to neighbors until convergence
Get nodes ranking as per the points accumulated(Page rank)
Compare the ranks obtaineed with the rank obtained with the inbuilt function
'''
import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np

def add_edges(G, p):
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r <= p:
                    G.add_edge(i,j)
    return G

def initialize_points(G):
    points = [100 for i in range(G.number_of_nodes())]
    return points


def distribute_points(G, points):
    prev_points = points
    new_points = [0]*G.number_of_nodes()
    for i in G.nodes():
        out = G.out_edges(i)
        if(len(out) == 0):
            new_points[i] += prev_points[i]
        else:
            share = prev_points[i]/len(out)
            for j in out:
                new_points[j[1]] += share
    return new_points
'''My version
def handle_point_sink(G, points,s = 0.8):
    No_out_nodes = []
    n = G.number_of_nodes()
    for i in range(n):
        if(G.out_edges(i) == 0):
            extra = points[i]*(1-s)
            for j in range(n):
                if G.nodes()[j] != i:
                    points[j] += extra
    return points
'''
def handle_point_sink(G, points, s = 0.8):

    No_out_nodes = []
    for i in range(len(points)):
        points[i] = points[i]*s
    n = G.number_of_nodes()
    extra = (n*100*0.2)/(n)
    for i in range(n):
        points[i] += extra
    return points

def keep_distributing_points(G, points):
    prev_points = points
    new = distribute_points(G, points)
    
    while(prev_points != new):
        prev_points = new
        new = distribute_points(G, new)
        new = handle_point_sink(G, new)
    print(new)
    print(prev_points)
    return new
def get_sorted_by_points(points):
    return np.argsort(- np.array(points))
def main():
    global G
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G = add_edges(G, 0.3)
    points = initialize_points(G)
    points = keep_distributing_points(G, points)
    nodes_sorted_by_points = get_sorted_by_points(points)
    print (nodes_sorted_by_points)
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse = True)
    for i in pr_sorted:
        print(i[0],end = " ")
    nx.draw(G,with_labels = True)
    plt.show()
    
main()
