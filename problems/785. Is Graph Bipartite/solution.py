# 785. Is Graph Bipartite?
from collections import defaultdict


class Solution:
    def isBipartite(self, A):
        n = len(A)

        g = defaultdict(list)
        for u in range(n):
            for v in A[u]:
                g[u].append(v)

        visited = defaultdict(lambda: 0)

        def dfs(u, color):
            if visited[u] > 0:
                return visited[u] == color
            visited[u] = color

            for v in g[u]:
                if not dfs(v, 3 - color):
                    return False

            return True

        for u in range(n):
            if visited[u] == 0:
                if not dfs(u, 1):
                    return False
        return True
