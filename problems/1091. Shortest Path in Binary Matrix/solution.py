# 1091. Shortest Path in Binary Matrix

class Solution:
    def shortestPathBinaryMatrix(self, M):
        n = len(M)
        if M[0][0] or M[n - 1][n - 1]:
            return -1

        #  8-directionally vector
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)]

        M[0][0] = 1
        q = [[0, 0, 1]]
        for i, j, k in q:
            if i == j == n - 1:
                return k
            for xdir, ydir in dirs:
                x, y = i + xdir, j + ydir
                if x < 0 or y < 0 or x >= n or y >= n or M[x][y]:
                    continue
                M[x][y] = 1
                q.append([x, y, k + 1])
        return -1
