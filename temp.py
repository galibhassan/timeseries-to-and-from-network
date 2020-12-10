import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# G = nx.complete_graph(100)
G = nx.fast_gnp_random_graph(1000, .3)
# G = nx.read_adjlist('test.adjlist')

degreeFreq = nx.degree_histogram(G)
degreesPossible = range(len(degreeFreq))
# plt.bar(np.arange(0, len(degreeFreq)), degreeFreq, width=0.1, color='lightgray', zorder=0)
# plt.scatter(np.arange(0, len(degreeFreq)), degreeFreq, zorder=1)
plt.bar(degreesPossible, degreeFreq, zorder=0 )
plt.scatter(degreesPossible, degreeFreq, zorder=1 )
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.show()
