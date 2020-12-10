import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# G = nx.complete_graph(100)
# G = nx.fast_gnp_random_graph(1000, .3)
# G = nx.read_adjlist('test.adjlist')
n = 10000
G = nx.scale_free_graph(n)

degreeFreq = np.array(nx.degree_histogram(G))/G.number_of_nodes()
degreesPossible = range(len(degreeFreq))
# plt.bar(degreesPossible, degreeFreq, zorder=0 )
# plt.scatter(degreesPossible, degreeFreq, zorder=1 )
plt.loglog(degreesPossible, degreeFreq, 'o', zorder=1 )
plt.ylabel('$p(K) = \dfrac{n_k}{\sum_k n_k}$')
plt.xlabel('k')
plt.title(f"nx.scale_free_graph({n})")
plt.show()
