# 821. Shortest Distance to a Character
class Solution:
    def shortestToChar(self, s, c):
        n = len(s)
        res, pos = [0] * n, 2 * n
        for i in reversed(range(n)):
            if s[i] == c:
                pos = i
            res[i] = pos - i

        pos = -2 * n
        for i in range(n):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], i - pos)

        return res
