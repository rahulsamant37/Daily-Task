"""
Graph Terminologies Overview

This documentation provides definitions of common terminologies used in graph theory:

1. **Graph (G)**: A collection of vertices (nodes) and edges (connections between nodes).
   - Notation: G = (V, E), where V is the set of vertices and E is the set of edges.

2. **Vertex (Node)**: A fundamental unit represented as a point in the graph. Vertices may store data.

3. **Edge**: A connection between two vertices. Can be:
   - **Directed** (arc): Edge has a direction, from one vertex to another.
   - **Undirected**: Edge has no direction; represents mutual connection.

4. **Adjacent Vertices (Neighbors)**: Two vertices connected by an edge.

5. **Degree**:
   - **Undirected Graph**: Number of edges connected to a vertex.
   - **Directed Graph**:
     - **In-degree**: Number of incoming edges to a vertex.
     - **Out-degree**: Number of outgoing edges from a vertex.

6. **Path**: A sequence of vertices where each adjacent pair is connected by an edge.
   - **Simple Path**: A path with no repeated vertices.
   - **Cycle**: A path that starts and ends at the same vertex, with no other repetitions.

7. **Connected Graph**: An undirected graph where there is a path between every pair of vertices.
   - **Strongly Connected**: In a directed graph, every vertex is reachable from every other vertex.
   - **Weakly Connected**: A directed graph is connected when ignoring edge directions.

8. **Tree**: A connected, acyclic undirected graph.

9. **Subgraph**: A graph formed from a subset of the vertices and edges of a larger graph.

10. **Weighted Graph**: A graph where edges have weights (costs, distances, etc.).

11. **Unweighted Graph**: A graph where all edges are considered equal.

12. **Multigraph**: A graph that allows multiple edges between the same pair of vertices.

13. **Loop**: An edge that connects a vertex to itself.

14. **Directed Acyclic Graph (DAG)**: A directed graph with no cycles.

These terms form the foundational language for working with and analyzing graph-based structures in computer science, mathematics, and related fields.
"""