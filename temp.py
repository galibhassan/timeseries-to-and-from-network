import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraphWeighted as vgw

# G = nx.complete_graph(100)
# G = nx.fast_gnp_random_graph(1000, .3)
# G = nx.read_adjlist('test.adjlist')
# n = 100
# G = nx.scale_free_graph(n)

G = nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edge(1,2, weight=1)
G.add_edge(1,3, weight=1)
G.add_edge(1,4, weight=1)
# G.add_edge(2,3, weight=1)
G.add_edge(2,4, weight=1)
G.add_edge(3,4, weight=1)


"""
for i in G.nodes:
    print("--")
    currentEdges = G.edges(i)
    for edge in currentEdges:
        a = G.get_edge_data(edge[0], edge[1])["weight"]
        print(a)
"""


wHist = vgw.getWeightHistogram(G)

#print(wHist)
plt.plot(wHist["x"], wHist["y"],'o')
plt.xlabel("Wights")
plt.ylabel("Count")
#plt.xticks(ticks=wHist["x"])

pos = nx.spring_layout(G)
plt.figure()
nx.draw(G,pos,edge_color='black',width=1,linewidths=1,\
node_size=500,node_color='pink',alpha=0.9,\
labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(G,pos,edge_labels={(1,2):12},font_color='red')
plt.axis('off')
plt.show()

""" 
print(nx.degree_histogram(G))
degreeFreq = np.array(nx.degree_histogram(G))/G.number_of_nodes()
degreesPossible = range(len(degreeFreq))
# plt.bar(degreesPossible, degreeFreq, zorder=0 )
# plt.scatter(degreesPossible, degreeFreq, zorder=1 )
plt.loglog(degreesPossible, degreeFreq, 'o', zorder=1 )
plt.ylabel('$p(K) = \dfrac{n_k}{n}$')
plt.xlabel('k')
plt.title(f"nx.scale_free_graph({n})")
plt.show()
"""
