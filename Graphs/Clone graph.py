"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        old = {}  # dictionary for remember old value

        def dfs(node):  # dfs
            if node in old:  # if node is already copied i need to return the new one as neighbors
                return old[node]
            new = Node(node.val)  # deep copy
            old[node] = new
            for x in node.neighbors:
                # for each node near the original i call the dfs and append the return value to the new one
                new.neighbors.append(dfs(x))
            return new

        return dfs(node) if node else None