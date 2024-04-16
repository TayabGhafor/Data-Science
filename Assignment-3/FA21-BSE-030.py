# 16 April, 2024
# CSC461 – Assignment3 – IDS – Graph Analysis
# Muhammad Tayab
# FA21-BSE-030
# There are two questions given in the Assignment-3 related to the Graph Analysis. 
#we have to solve them using graphs concepts.

'''
Question-1:
               Using the networkx library in Python, create an undirected graph described by the adjacency matrix shown
          below. Once the graph is constructed, draw it to see if there is a loop in the graph? If yes, at which point?

'''

import networkx as nx
import matplotlib.pyplot as plt
# Adjacency matrix
adjacency_matrix = [
    [0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
]

# Creating empty graph
G = nx.Graph()
# Adding nodes
nodes = ["a", "b", "c", "d", "e", "f", "g"]
G.add_nodes_from(nodes)
# Adding edges 
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if adjacency_matrix[i][j] == 1:
            G.add_edge(nodes[i], nodes[j])
# Drawing graph
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
# Checking for loops

loops = list(nx.simple_cycles(G))
if loops:
    print("There is a loop in the graph.")
    print("The loop occurs at node(s):", loops)
else:
    print("There are no loops in the graph.")


'''
  Question-2:
              Assign random weights to the edges in the graph created in Q1. Once the weights are assigned, run Dijkstra
              to find out shortest path between A and B. Print both shortest path and the length of the shortest path.

'''
# to Assign random weights to edges
import random
# Creating weighted graph
weighted_G = G.copy()
for u, v in weighted_G.edges():
    weighted_G[u][v]['weight'] = random.randint(1, 10)
# Drawing the weighted graph
pos = nx.spring_layout(weighted_G) 
nx.draw(weighted_G, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(weighted_G, 'weight')
nx.draw_networkx_edge_labels(weighted_G, pos, edge_labels=labels)
plt.show()
# Using Dijkstra's algorithm to find the shortest path between A and B
shortest_path = nx.shortest_path(weighted_G, source='a', target='b', weight='weight')
shortest_path_length = nx.shortest_path_length(weighted_G, source='a', target='b', weight='weight')
# Printing the Results
print("Shortest path between A and B:", shortest_path)
print("Length of the shortest path:", shortest_path_length)
