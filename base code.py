import networkx as nx
import matplotlib.pyplot as plt
import random

'''
G = nx.erdos_renyi_graph(10,0.5)
nx.write_gml(G, 'random_graph.gml')
'''
def set_nodes_A(G,*nodes):
    for each in nodes:
        G.node[each]['action'] = 'A'
def set_all_B(G):
    for each in G.nodes():
        G.node[each]['action'] = 'B'
def Color_it(G):
    list1 = []
    for each in G.nodes():
        if G.node[each]['action'] == 'A':
            list1.append('green')
        else:
            list1.append('red')
    return list1
def find_neigh(each,c,G):
    num = 0
    for each1 in G.neighbors(each):
        if G.node[each1]['action'] == c:
            num+=1
    return num
def recalculate_option(G):
    dict1 = {}
    a = 4
    b = 3
    for each in G.nodes():
        num_A = find_neigh(each,'A',G)
        num_B = find_neigh(each,'B',G)
        payoff_A = a*num_A
        payoff_B = b*num_B
        if payoff_A >= payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each] = 'B'
    return dict1
def reset_node_attribute(G,action_dict):
    for each in action_dict:
        G.node[each]['action'] = action_dict[each]

#G = nx.read_gml('random_graph.gml')
G = nx.erdos_renyi_graph(10,0.5)
set_all_B(G)
set_nodes_A(G,3,7)
colors = Color_it(G)
nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
plt.show()

action_dict = recalculate_option(G)
reset_node_attribute(G,action_dict)
colors = Color_it(G)
nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
plt.show()
