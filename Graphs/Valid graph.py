class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n, edges):

        if not n:
            return True
        dic = {i: [] for i in range(n)}
        visited = set()
        for n1, n2 in edges:
            dic[n1].append(n2)
            dic[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for x in dic[node]:
                if x != prev:
                    if not dfs(x, node):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)

        #dfs on the first node for cycle check and then we check len of visisted for see if there are
        #not connected component