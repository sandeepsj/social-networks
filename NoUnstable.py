import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def getTrias(G):
    nodes = G.nodes()
    tris_list = [list(x) for x in itertools.combinations(nodes,3)]
    return tris_list
#4.2.store the sign details of all the triangles
def get_signs_of_tris(tris_list, G):
    all_signs = []
    for i in range(len(tris_list)):
        temp = []
        temp.append(G[tris_list[i][0]][tris_list[i][1]]['sign'])
        temp.append(G[tris_list[i][1]][tris_list[i][2]]['sign'])
        temp.append(G[tris_list[i][2]][tris_list[i][0]]['sign'])
        all_signs.append(temp)
    return all_signs

#4.3.Count the number of unstable triangles in the network.
def count_unstable(all_signs):
    stable = 0
    unstable = 0
    for i in all_signs:
        if i.count('+') == 3 or i.count('+') == 1:
            stable += 1
        elif i.count('+') == 2 or i.count('+') == 0:
            unstable += 1
    #print ('Number of stable triangle out of ',stable+unstable, 'are', stable)
    #print ('Number of unstable triangle out of ',stable+unstable, 'are', unstable)
    return unstable

#--------------------------------------------
G = nx.complete_graph(5)
nx.set_edge_attributes(G, {(0,1): {'sign': '+'}, (0,2): {'sign': '+'}, (0,3): {'sign': '+'}, (0,4): {'sign': '-'}, (1,2): {'sign': '+'}, (1,3): {'sign': '+'}, (1,4): {'sign': '+'}, (2,3): {'sign': '-'}, (2,4): {'sign': '+'}, (3,4): {'sign': '+'}})

tris_list = getTrias(G)
all_signs = get_signs_of_tris(tris_list, G)
unstable = count_unstable(all_signs)
unstable_track = [unstable]
print(unstable)
