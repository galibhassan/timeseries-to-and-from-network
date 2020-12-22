from scipy.io import loadmat
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraphWeighted as vgw
from scipy.stats import levy_stable

data = loadmat('./fractaldata/fractaldata.mat')
data_multifractal_ihlen = np.array(data["multifractal"]) 
# data_monofractal = np.array(data["monofractal"])
# data_whitenoise = np.array(data["whitenoise"])

alpha = 1.5
size = 10000
data_multifractal = levy_stable.rvs(alpha=alpha, beta = 0, size=size)
plt.plot(np.sqrt(data_multifractal**2))
plt.show()


PLOT_DIR_PATH = './plots/multifractal/weighted/levyStable/squared'
GRAPH_DIR_PATH = './generatedGraphs/multifractal/weighted/levyStable/squared'

indices = np.arange(100, len(data_multifractal), 500)
for i in indices:
    test_multifractal_ts = data_multifractal[0:i]
    test_multifractal_t = np.arange(0, len(test_multifractal_ts))

    visGraph = vgw.getVisibilityGraph(test_multifractal_t, test_multifractal_ts, options={"visualize": False})
    nNodes = visGraph.number_of_nodes()
    nEdges = visGraph.number_of_edges()
    filename = f'levyStable__{test_multifractal_t[0]}_{test_multifractal_t[-1]}_weighted_squared'
    nx.write_weighted_edgelist(visGraph, f'{GRAPH_DIR_PATH}/{filename}')

    # degreeFreq = np.array(nx.degree_histogram(visGraph))/visGraph.number_of_nodes()
    # degreesPossible = range(len(degreeFreq))
    # plt.bar(degreesPossible, degreeFreq, zorder=0 )
    # plt.scatter(degreesPossible, degreeFreq, zorder=1 )


    wHist=vgw.getWeightHistogram(visGraph)
    plt.loglog(wHist["x"], wHist["y"], 'o')
    plt.xlabel("Combined edge-weight for one node")
    plt.ylabel("Count")
    plt.title(f"Edge-weight distribution of {filename} \n #Nodes={nNodes}, #Edges={nEdges}")
    imageFileName=f'{PLOT_DIR_PATH}/{filename}.png'
    plt.savefig(imageFileName, dpi = None, facecolor = 'w', edgecolor = 'w',
                orientation = 'portrait', papertype = None, format = None,
                transparent = False, bbox_inches = None, pad_inches = 0.1,
                metadata = None)
    plt.clf()
    