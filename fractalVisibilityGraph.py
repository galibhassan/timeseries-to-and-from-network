from scipy.io import loadmat
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import visibilityGraph as vg

def getRMS(ts):
    rms  = np.sqrt(np.mean(ts**2))
    return rms

data = loadmat('./fractaldata/fractaldata.mat')
data_multifractal = np.array(data["multifractal"]) 
data_monofractal = np.array(data["monofractal"])
data_whitenoise = np.array(data["whitenoise"])

test_monofractal_ts = data_monofractal[0:100]
test_monofractal_t = np.arange(0, len(test_monofractal_ts))


visGraph = vg.getVisibilityGraph(test_monofractal_t, test_monofractal_ts, options={"visualize": False})
filename = f'ihlen_monofractal__{test_monofractal_t[0]}_{test_monofractal_t[-1]}'
nx.write_adjlist(visGraph, f'./generatedGraphs/monofractal/{filename}')




plt.plot(test_monofractal_t, test_monofractal_ts)
plt.title(filename)
PLOT_DIR_PATH = './plots/monofractal'
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
plt.title(f'Degree distribution of {filename}')
plt.tight_layout()
imageFileName = f'{PLOT_DIR_PATH}/degreeDist/{filename}.png'
plt.savefig(imageFileName, dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format=None,
            transparent=False, bbox_inches=None, pad_inches=0.1,
            metadata=None)



# plt.show()
