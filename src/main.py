import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

G = nx.Graph()
G.add_edges_from(edge_list)

nx.draw_spring(G, with_labels=True)
plt.show()
plt.savefig("graph.png")