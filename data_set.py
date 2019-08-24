import networkx as nx
import matplotlib.pyplot as plt
#G=nx.read_edgelist('datasets/facebook_combined.txt')
#G=nx.read_pajek('datasets/football.net')
#G=nx.read_gexf('datasets/EuroSiS Generale Pays.gexf')
G=nx.read_gml('datasets/karate.gml',label='id')
#print (nx.info(G))
#print (nx.number_of_nodes(G))
#print (nx.number_of_edges(G))
#print (nx.is_directed(G))

#plt.show()
def plot_deg_dist(G):
    all_degree=[val for (node,val) in nx.degree(G)]
    unique_degrees=list(set(all_degree))
    count_of_degrees=[]
    for i in unique_degrees:
        x=all_degree.count(i)
        count_of_degrees.append(x)
    plt.plot(unique_degrees,count_of_degrees,'yo-')
    plt.xlabel('Degrees')
    plt.ylabel('Number of nodes')
    plt.title('Degree distribution of karate nettwork')
    plt.show()
for i in nx.clustering(G).items():
    print (i)
print (nx.average_clustering(G))
