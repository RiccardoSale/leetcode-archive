#You have a graph of n nodes.
#You are given an integer n and an array edges where edges[i] = [ai,bi]
# indicates that there is an edge between ai and bi in the graph
#Return number of connected Components "PART OF THE GRAPH NOT CONNECTED"

#dfs search from one node mark the visited
#and continue with the for loop for search the other
#its like "number of island "

#complex O(e+v)
#or we can use UNION FIND algorithm

class Solution:
    def countComponents(self, n:int, edges:List[List[int]]) -> int:

        visited = set()
        map = {i: [] for i in range(len(edges))}
        for n1,n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)
        #create adj list

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for x in map[node]:
                dfs(x)
            return 1

        res = 0
        for x in edges:
            if dfs(x[0]):
                res += 1
        return res


