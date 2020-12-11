from scipy.io import loadmat
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraph as vg

data = loadmat('./fractaldata/fractaldata.mat')
data_multifractal = np.array(data["multifractal"]) 
data_monofractal = np.array(data["monofractal"])
data_whitenoise = np.array(data["whitenoise"])


indices = np.arange(2100, len(data_multifractal), 500)
for i in indices:
    test_multifractal_ts = data_multifractal[0:i]
    test_multifractal_t = np.arange(0, len(test_multifractal_ts))


    visGraph = vg.getVisibilityGraph(test_multifractal_t, test_multifractal_ts, options={"visualize": False})
    nNodes = visGraph.number_of_nodes()
    nEdges = visGraph.number_of_edges()
    filename = f'ihlen_multifractal__{test_multifractal_t[0]}_{test_multifractal_t[-1]}'
    nx.write_adjlist(visGraph, f'./generatedGraphs/multifractal/{filename}')


    plt.plot(test_multifractal_t, test_multifractal_ts)
    plt.title(filename)
    PLOT_DIR_PATH = './plots/multifractal'
    imageFileName = f'{PLOT_DIR_PATH}/ts/{filename}.png'
    plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)

    plt.clf()
    degreeFreq = np.array(nx.degree_histogram(visGraph))/visGraph.number_of_nodes()
    degreesPossible = range(len(degreeFreq))
    # plt.bar(degreesPossible, degreeFreq, zorder=0 )
    # plt.scatter(degreesPossible, degreeFreq, zorder=1 )
    plt.loglog(degreesPossible, degreeFreq, 'o', zorder=1 )
    plt.ylabel('$p(K) = \dfrac{n_k}{\sum_k n_k}$')
    plt.xlabel('k')
    plt.title(f'Degree distribution of {filename} \n #Nodes={nNodes}, #Edges={nEdges}')
    plt.tight_layout()
    imageFileName = f'{PLOT_DIR_PATH}/degreeDist/{filename}.png'
    plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)



    # plt.show()
