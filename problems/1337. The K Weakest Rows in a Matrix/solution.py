# 1337. The K Weakest Rows in a Matrix
from collections import defaultdict


class Solution:
    def kWeakestRows(self, M, k):
        m, n = len(M), len(M[0])
        res, visited = [], defaultdict(bool)

        for j in range(n):
            for i in range(m):
                if not visited[i] and not M[i][j]:
                    visited[i] = True
                    res.append(i)
                    if len(res) == k:
                        return res

        for i in range(m):
            if not visited[i]:
                res.append(i)
                if len(res) == k:
                    return res

        return res
