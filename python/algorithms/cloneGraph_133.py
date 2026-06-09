"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class SolutionDFS:

    def __init__(self):
        # Save the visited node as key, and the clone reference
        # as the value in a dictionary
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node


        # If the node was already visited, return the clone
        if node in self.visited:
            return self.visited[node]


        # Create a clone for the current node w/ empty neighbors
        clone_node = Node(node.val,[])

        # Then add the node-clone key-value pair to dict
        self.visited[node] = clone_node

        # Then go through the nodes neighbors
        # Call this function again on each node neighbor
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(neighbor_node) for neighbor_node in node.neighbors]

        return clone_node


class SolutionBFS:
    pass