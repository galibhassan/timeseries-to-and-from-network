import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def isVisible(ta, ya, tb, yb, tc, yc):
    heightLimit = yb + (ya-yb)*(tb-tc)/(tb-ta)
    if(yc < heightLimit):
        return True
    else:
        return False


def getVisibilityGraph(t, ts, options={
    "visualize": False,
}):
    myRed = "#f49a8e"
    myBlue = "#6875eb"

    visGraph = nx.Graph()
    for i in range(len(ts)):
        visGraph.add_node(i)
        for j in range(i+1, len(ts)):
            tsInBetween = ts[i+1:j]
            if len(tsInBetween) == 0:
                # i, j consecutive indices; so visible
                if options["visualize"] == True:
                    
                    plt.plot([t[i], t[j]], [ts[i], ts[j]],
                             color=myBlue, zorder=200)
                edgeWeight = np.abs(ts[j]-ts[i])
                visGraph.add_edge(i, j, weight=edgeWeight)
            elif len(tsInBetween) > 0:
                stillVisible = True
                for k in range(len(tsInBetween)):
                    visFlag = isVisible(
                        t[i], ts[i], t[j], ts[j], t[i+1+k], tsInBetween[k])
                    if visFlag == False:
                        if options["visualize"] == True:
                            plt.plot([t[i], t[j]], [ts[i], ts[j]],
                                     color="#d4dde3", zorder=199)
                        stillVisible = False
                        break

                if stillVisible == True:
                    if options["visualize"] == True:
                        plt.plot([t[i], t[j]], [ts[i], ts[j]],
                                 color=myBlue, zorder=200)
                    edgeWeight = np.abs(ts[j]-ts[i])
                    visGraph.add_edge(i, j, weight=edgeWeight)

    if options["visualize"] == True:
        plt.bar(t.reshape(len(t)), ts.reshape(len(ts)),
                width=.05, zorder=99, color=myRed)
        plt.scatter(t.reshape(len(t)), ts.reshape(
            len(ts)), zorder=300, color="#242444")
        plt.show()
    return visGraph


def getWeightHistogram(G):
    weightsArray = []
    nodesArray = []
    weightedDegreeCount = G.degree(weight="weight")
    for pair in weightedDegreeCount:
        nodesArray.append(pair[0])    
        weightsArray.append(pair[1])

    weightsArrayNp = np.array(weightsArray)
    hist, bin_edges = np.histogram(weightsArrayNp, bins=len(weightsArray), range=(0, weightsArrayNp.max()))

    return {"y": np.array(hist), "x": np.array(bin_edges[1:])}

