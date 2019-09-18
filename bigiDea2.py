import networkx as nx
import matplotlib.pyplot as plt
import random

'''
G = nx.erdos_renyi_graph(10,0.5)
nx.write_gml(G, 'random_graph.gml')
'''
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
    a = 10
    b = 6
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
G = nx.erdos_renyi_graph(10,0.5)

for u in G.nodes():
    for v in G.nodes():
        if u < v:

            set_all_B(G)
            #init_nodes =  [ 3,7]
            set_nodes_A(G,[u,v])
            colors = Color_it(G)
            #nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            #plt.show()
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
                print(u,v,': cascade is complete')
            else:
                print (u,v ,': cascade is incomplete')
            #nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            #plt.show()
