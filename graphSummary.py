import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def getGraphSummary(graphPath):
   G = nx.read_weighted_edgelist(graphPath)
   print(G)


# test
GRAPH_DIR = './generatedGraphs/multifractal/weighted/'
GRAPH_FILENAME = 'ihlen_multifractal__0_2099_weighted'
graphPath = f"{GRAPH_DIR}/{GRAPH_FILENAME}"

getGraphSummary(graphPath)
