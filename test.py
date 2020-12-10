import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraph as vg


GRAPH_DIR_PATH = 'generatedGraphs'
PLOT_DIR_PATH = GRAPH_DIR_PATH

t = np.arange(0, 3*np.pi, np.pi/10)
ts = np.sin(t)
fileName = 'sin(t)__0-3pi__0.1pi'
visGraph = vg.getVisibilityGraph(t, ts, options={"visualize": False})
nx.write_adjlist(visGraph, f'{GRAPH_DIR_PATH}/{fileName}.adjlist')

degreeFreq = nx.degree_histogram(visGraph)
degreesPossible = range(len(degreeFreq))
plt.bar(degreesPossible, degreeFreq, zorder=0, width=0.1)
plt.scatter(degreesPossible, degreeFreq, zorder=1)
plt.xlabel('Degree')
plt.ylabel('Frequency')

imageFileName = f'{PLOT_DIR_PATH}/{fileName}.png'
plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)