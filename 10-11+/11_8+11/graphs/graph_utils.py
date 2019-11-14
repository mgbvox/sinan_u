import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def rand_network(n=10,e=18):
    simple_network = nx.Graph()

    nodes = np.arange(n)
    edges = set(list(zip(*np.random.randint(0, n, (2, e)))))

    simple_network.add_nodes_from(nodes)
    simple_network.add_edges_from(edges)

    return simple_network