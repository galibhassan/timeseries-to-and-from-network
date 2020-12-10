import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraph as vg


GRAPH_DIR_PATH = 'generatedGraphs'
PLOT_DIR_PATH = 'plots'

indices = np.arange(3, 300, 2)
interval = 0.1
for i in indices:
    t = np.arange(0, i*np.pi, interval*np.pi)
    ts = np.sin(t)
    fileName = f'sin(t)__0-{i}pi__{interval}pi'
    visGraph = vg.getVisibilityGraph(t, ts, options={"visualize": False})
    nx.write_adjlist(visGraph, f'{GRAPH_DIR_PATH}/{fileName}.adjlist')

    degreeFreq = nx.degree_histogram(visGraph)
    degreesPossible = range(len(degreeFreq))
    # plt.bar(degreesPossible, degreeFreq, zorder=0, width=0.1)
    plt.plot(degreesPossible, degreeFreq, 'o-', zorder=1)
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title(
        f"Degree frequency of f(t)=sin(t) visibility graph \nin [0, {indices[0]} to {i}*pi] with {interval} t-increment \n#Node = {visGraph.number_of_nodes()}, #Edges = {visGraph.number_of_edges()}")

    imageFileName = f'{PLOT_DIR_PATH}/{fileName}.png'
    plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
