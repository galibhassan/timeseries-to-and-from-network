from scipy.io import loadmat
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraphWeighted as vgw
from scipy.stats import levy_stable
import os

# constants
PLOT_DIR_PATH = "./plots/multifractal/weighted/levyStable/signFlipped_and_unflipped"
GRAPH_DIR_PATH = (
    "./generatedGraphs/multifractal/weighted/levyStable/signFlipped_and_unflipped"
)

outputDirs = [PLOT_DIR_PATH, GRAPH_DIR_PATH]
for dir in outputDirs:
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print("exists: ", dir)

# generate timeseries with maltifractality by levy process
alpha = 1.5
size = 10000
data_multifractal = levy_stable.rvs(alpha=alpha, beta=0, size=size)

# loop to generate visibility graphs for different node-counts
nodeCount_lowest = 100
nodeCount_highest = len(data_multifractal)
lastIndices = np.arange(nodeCount_lowest, nodeCount_highest, 500)

for lastIndex in lastIndices:
    test_multifractal_ts = data_multifractal[0:lastIndex]
    test_multifractal_ts_signFlipped = -test_multifractal_ts
    test_multifractal_t = np.arange(0, len(test_multifractal_ts))

    # generate weighted visibility graph
    visGraph = vgw.getVisibilityGraph(
        test_multifractal_t, test_multifractal_ts, options={"visualize": False}
    )
    nNodes = visGraph.number_of_nodes()
    nEdges = visGraph.number_of_edges()

    visGraph_signFlipped = vgw.getVisibilityGraph(
        test_multifractal_t,
        test_multifractal_ts_signFlipped,
        options={"visualize": False},
    )

    # export graph data
    filenameToSave = (
        f"levyStable__{test_multifractal_t[0]}_{test_multifractal_t[-1]}_weighted"
    )
    filenameToSave_signFlipped = f"{filenameToSave}_signFlipped"

    nx.write_weighted_edgelist(visGraph, f"{GRAPH_DIR_PATH}/{filenameToSave}")
    nx.write_weighted_edgelist(
        visGraph_signFlipped, f"{GRAPH_DIR_PATH}/{filenameToSave_signFlipped}"
    )

    # compute weighted histogram
    weightedHist = vgw.getWeightHistogram(visGraph)
    weightedHist_signFlipped = vgw.getWeightHistogram(visGraph_signFlipped)

    # plot
    plt.loglog(
        weightedHist["x"], weightedHist["y"], "o", label="Sign unflipped", markersize=3
    )
    plt.loglog(
        weightedHist_signFlipped["x"],
        weightedHist_signFlipped["y"],
        "o",
        label="Sign flipped",
        markersize=3,
    )
    plt.legend()
    plt.xlabel("Combined edge-weight for one node")
    plt.ylabel("Count")
    plt.title(
        f"Edge-weight distribution of {filenameToSave} \n #Nodes={nNodes}, #Edges={nEdges}"
    )

    # save plot
    imageFileName = f"{PLOT_DIR_PATH}/{filenameToSave}.png"
    plt.savefig(
        imageFileName,
        dpi=300,
        facecolor="w",
        edgecolor="w",
        orientation="portrait",
        papertype=None,
        format=None,
        transparent=False,
        bbox_inches=None,
        pad_inches=0.1,
        metadata=None,
    )
    plt.clf()
