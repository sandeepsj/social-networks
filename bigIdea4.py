import networkx as nx
import random
import matplotlib.pyplot as plt

def set_nodes_A(G,nodes):
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
    a = 3
    b = 2
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
def terminate_1(c,G):
    for i in G.nodes():
        if G.node[i]['action']!= c:
            return 0
    return 1
def terminate(G, count):
    flag1 = terminate_1('A',G)
    flag2 = terminate_1('B',G)
    if (flag1 == 1 or flag2 ==1 or count>100):
        return 1
    else:
        return 0
#G = nx.read_gml('random_graph.gml')
#G = nx.erdos_renyi_graph(10,0.5)



def create_first_community(G):
    for i in range(0,10):
        G.add_node(i)
    for i in range(0,10):
        for j in range(0,10):
            if i < j:
                p = 0.5
                r = random.uniform(0,1)
                if r < p:
                    G.add_edge(i,j)
def create_second_community(G):
    for i in range(11,20):
        G.add_node(i)
    for i in range(11,20):
        for j in range(11,20):
            if i < j:
                p = 0.5
                r = random.uniform(0,1)
                if r < p:
                    G.add_edge(i,j)

                    
G = nx.Graph()

G.add_edges_from([(0,1),(0,6),(1,2),(1,8),(1,12),(2,12),(3,4),(3,12),(3,9),(4,5),(4,12),(5,6),(5,10),(6,8),(7,8),(7,9),(7,10),(7,11),(8,9),(8,10),(8,11),(9,10),(9,11),(10,11)])
set_all_B(G)

list2 = [[0,1,2,3],[0,2,3,4],[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,12],[2,3,4,12],[0,1,2,3,4,5],[0,1,2,3,4,5,6,12]]
for init_nodes in list2:
    set_nodes_A(G,init_nodes)
    colors = Color_it(G)
    nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
    plt.show()
    flag = 0 
    count = 0
    while (1):
        flag = terminate(G,count)
        if (flag):
            break
        count += 1
        action_dict = recalculate_option(G)
        reset_node_attribute(G,action_dict)
        colors = Color_it(G)
    c = terminate_1('A',G)
    if c:
        print(init_nodes,': cascade is complete')
    else:
        print (init_nodes,': cascade is incomplete')
    nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
    plt.show()
