#The friend of my friend is my friend
#Two friends have one common enemy
#Enemy of my friend is my enemy
#Friend of my enemy is my enemy
'''
Aim:networks of countries enemity or friends network
1.Network starts from an unstable state and gradually moves to stable state
2.Once the network becomes stable then convert into team by considering clusters of friends together

    1.Create a graph with 'n' nodes,where the nodes are the countries
    2.Make it a complete graph by adding all possible edges.Also, assigne '+' or '-' signs as weights to all the edges randomly
    3.Display the network

    4.
        1.Get a listof all the triangle in the network
        2.store the sign details of all the triangles
        3.Count the number of unstable triangles in the network.
    5.While the number of unstable traingles in not zero,do the following
        1.Choose a triangle in the graph that is unstable.
        2.Make that triangle stable.
        3.Count the number of unstable triangles.
    6.Now that there is no unstable triangle in the network, it can be divided into two coalitions,such that in each coalition, the intra-edges are positive, and the inter-edges are negative.
        1.Choose a random node. Add it to the first coalition.
        2.Also put all the friends of this node in the first coalition.
        3.Put all the enemies of this node in the second coalition.
        4.Repeat steps 6.2 and 6.3 for all the 'unprocessed' nodes of first coalition.
    7.Display the network with coalitions
    8.Minimum cost transformation
'''
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

#1.Create a graph with 'n' nodes,where the nodes are the countries
def create_Graph(n):
    G = nx.Graph()
    G.add_nodes_from(range(1,n+1))
    mapping = {1:'Alexancra',2:'Anterim',3:'Bercy', 4:'Bearland', 5: 'Eplex', 6: 'Gripa', 7: 'Ikly', 8:'Jemra', 9: 'Lema', 10: 'Umesi', 11: 'Mexim', 12: 'Socialcity', 13: 'Tersi', 14: 'Xopia', 15: 'Tamara'}
    G = nx.relabel_nodes(G, mapping)
    return G
#2.Make it a complete graph by adding all possible edges.Also, assigne '+' or '-' signs as weights to all the edges randomly
def Complete_and_Assign_Sign(G):

    signs = ['+', '-']
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                G.add_edge(i, j, sign = random.choice(signs))
            
#3.Display the network
def display(G):
    edge_labels = nx.get_edge_attributes(G, 'sign')
    pos = nx.circular_layout(G)
    nx.draw(G, pos, node_size = 5000,with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20, font_color = 'red')
    plt.show()

#USE THE FUNCTIONS
#--------------------------------------------
G = create_Graph(8)
Complete_and_Assign_Sign(G)
display(G)
#--------------------------------------------
    
#4.

#4.1.Get a listof all the triangle in the network
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

tris_list = getTrias(G)
all_signs = get_signs_of_tris(tris_list, G)
unstable = count_unstable(all_signs)
unstable_track = [unstable]
#--------------------------------------------
#2.Make that triangle stable.
def make_stable(G, tris_list, all_signs):
    found_unstable = False
    while(found_unstable == False):
        index = random.randint(0,len(tris_list)-1)#1.Choose a triangle in the graph that is unstable.
        if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0:
            found_unstable = True
        r = random.randint(1,3)
        if all_signs[index].count('+') == 0:
            if r == 1:
                G[tris_list[index][0]][tris_list[index][1]]['sign'] = '+'
            if r == 2:
                G[tris_list[index][1]][tris_list[index][2]]['sign'] = '+'
            if r == 3:                
                G[tris_list[index][2]][tris_list[index][0]]['sign'] = '+'
        elif all_signs[index].count('+') == 2:
            if r == 1:
                if G[tris_list[index][0]][tris_list[index][1]]['sign'] == '+':
                    G[tris_list[index][0]][tris_list[index][1]]['sign'] = '-'
                elif G[tris_list[index][0]][tris_list[index][1]]['sign'] == '-':
                    G[tris_list[index][0]][tris_list[index][1]]['sign'] = '+'
            elif r == 2:
                if G[tris_list[index][1]][tris_list[index][2]]['sign'] == '+':
                    G[tris_list[index][1]][tris_list[index][2]]['sign'] = '-'
                elif G[tris_list[index][1]][tris_list[index][2]]['sign'] == '-':
                    G[tris_list[index][1]][tris_list[index][2]]['sign'] = '+'
            elif r == 3:
                if G[tris_list[index][2]][tris_list[index][0]]['sign'] == '+':
                    G[tris_list[index][2]][tris_list[index][0]]['sign'] = '-'
                elif G[tris_list[index][2]][tris_list[index][0]]['sign'] == '-':
                    G[tris_list[index][2]][tris_list[index][0]]['sign'] = '+'
    #display(G)
    return G

#5.While the number of unstable traingles in not zero,do the following       
#--------------------------------------------
while(unstable !=0 ):
    G = make_stable(G, tris_list, all_signs)#2.Make that triangle stable.
    all_signs = get_signs_of_tris(tris_list, G)
    #print (all_signs)
    unstable = count_unstable(all_signs)#3.Count the number of unstable triangles.
    unstable_track.append(unstable)
plt.bar([i for i in range(len(unstable_track))],unstable_track)
plt.show()
#--------------------------------------------

#6.Now that there is no unstable triangle in the network, it can be divided into two coalitions,such that in each coalition, the intra-edges are positive, and the inter-edges are negative.


def see_coalitions(G):
    first_coalition = []
    second_coalition = []
    
    #6.1.Choose a random node. Add it to the first coalition.
    nodes = list(G.nodes())
    r = random.choice(nodes)
    first_coalition.append(r)

    #2.Also put all the friends of this node in the first coalition.
    processed_nodes = []
    to_be_processed = [r]

    for each in to_be_processed:
        if  each not in processed_nodes:
            neigh = G.neighbors(each)
            for i in neigh:
                if G[each][i]['sign'] == '+':
                    if G[each][i] not in first_coalition:
                        first_coalition.append(i)
                    if G[each][i] not in to_be_processed:
                        to_be_processed.append(i)
                elif G[each][i]['sign'] == '-':
                    if i not in second_coalition:
                        second_coalition.append(i)
                        processed_nodes.append(i)
            processed_nodes.append(each)
    return first_coalition, second_coalition
first, second = see_coalitions(G)
print(first)
print(second)

#7.Display the network with coalitions
edge_labels = nx.get_edge_attributes(G, 'sign')
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, first, 3000, "red", alpha = 0.8)
nx.draw_networkx_nodes(G, pos, second, 3000, "blue", alpha = 0.8)
nx.draw_networkx_labels(G, pos, font_size = 10)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 20, font_color = "green")
plt.show()
