## MST

Minnimum spanning tree is 
1. a subset of a edges of connected, edge-weighted undirected graph.
2. connects all nodes
3. without cycle
4. as little as total weight as possible
If there are n nodes, there will be n - 1 edges.

## Kruskal's Algorithm
Algorithm to find the Minimum Spanning Tree in the Graph. We sort the edges by weight in non - descending order and loop sorted edges, pick the edge as long as there are no connectivity already set up between two nodes and add this edge weight to the total weight.

Disjoint Set: The data structure used to check the connectivity of graph efficiently in dynamic by union the nodes into one set, and find the number of disconnected sets.

### Kruskal's Algorithm
1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

## Prim's Algorithm
1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3. Repeat step 2 (until all vertices are in the tree).
