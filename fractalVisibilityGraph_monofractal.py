from scipy.io import loadmat
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraphWeighted as vgw

data = loadmat('./fractaldata/fractaldata.mat')
# data_multifractal = np.array(data["multifractal"])
data_monofractal = np.array(data["monofractal"])
# data_whitenoise = np.array(data["whitenoise"])

indices = np.arange(100, 2200, 400)
for i in indices:
    test_monofractal_ts = data_monofractal[0:i]
    test_monofractal_t = np.arange(0, len(test_monofractal_ts))

    visGraph = vgw.getVisibilityGraph(
        test_monofractal_t, test_monofractal_ts, options={"visualize": False})
    filename = f'ihlen_monofractal__{test_monofractal_t[0]}_{test_monofractal_t[-1]}_weighted'
    nx.write_weighted_edgelist(
        visGraph, f'./generatedGraphs/monofractal/weighted/{filename}')

    plt.clf()
    plt.plot(test_monofractal_t, test_monofractal_ts)
    plt.title(filename)
    PLOT_DIR_PATH = './plots/monofractal'
    imageFileName = f'{PLOT_DIR_PATH}/ts/{filename}.png'
    plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                metadata=None)
    plt.clf()


    # plt.plot(wHist["x"], wHist["y"], 'o')
    # plt.loglog(wHist["x"], wHist["y"], 'o', zorder = 1)
    # plt.xlabel('k')
    # plt.title(f'Degree distribution of {filename}')
    # plt.tight_layout()
    wHist=vgw.getWeightHistogram(visGraph)
    plt.plot(wHist["x"], wHist["y"], 'o')
    plt.xlabel("Combined weights for one node")
    plt.ylabel("Count")

    imageFileName=f'{PLOT_DIR_PATH}/weightDist/{filename}.png'
    plt.savefig(imageFileName, dpi = None, facecolor = 'w', edgecolor = 'w',
                orientation = 'portrait', papertype = None, format = None,
                transparent = False, bbox_inches = None, pad_inches = 0.1,
                metadata = None)
    plt.clf()
