
import networkx as nx
import matplotlib.pyplot as plt

import jonson as jon

with open('inputs.txt', 'r') as inputs:
    global graph
    graph = []

    for line in inputs:
        graph.append(tuple(line[:-1].split(', ')))


graph = [(int(i[0]), int(i[1]), int(i[2])) for i in graph]


G = nx.DiGraph()
G.add_weighted_edges_from(graph)
pos = nx.planar_layout(G)


nx.draw(G, with_labels='True', pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))


vertices = set()
for i in graph:
    vertices.add(i[0])
    vertices.add(i[1])
size = len(vertices)
print(size)
print(graph)

path = jon.jon(size, graph, 0, 3)
print(path)
path = [(path[i], path[i+1]) for i in range(len(path)-1)]

nx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color='red')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.show()