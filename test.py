import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraphWeighted as vgs

GRAPH_DIR_PATH = 'generatedGraphs/sin(t)/vgw'
PLOT_DIR_PATH = 'plots/sin(t)/vgw'

indices = np.arange(3, 60, 2)
interval = 1
for i in indices:
    t = np.arange(0, i*np.pi, interval*np.pi)
    ts = np.sin(t)
    fileName = f'sin(t)__0-{i}pi__{interval}pi__weighted'
    visGraph = vgs.getVisibilityGraph(t, ts, options={"visualize": True})
    nx.write_weighted_edgelist(visGraph, f'{GRAPH_DIR_PATH}/{fileName}.edgelist')

    wHist = vgs.getWeightHistogram(visGraph)
    plt.clf()
    plt.plot(wHist["x"], wHist["y"], 'o')
    plt.xlabel("Combined weights for one node")
    plt.ylabel("Count")
    plt.title(
        f"Edge-weight distribution of nodes of f(t)=sin(t) weighted visibility graph \nin [0, {indices[0]} to {i}*pi] with {interval} t-increment \n#Node = {visGraph.number_of_nodes()}, #Edges = {visGraph.number_of_edges()}")

    imageFileName = f'{PLOT_DIR_PATH}/{fileName}.png'
    plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
    plt.clf()
