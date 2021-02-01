# 191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n):
        s = 0
        while n > 0:
            s += n & 1
            n = n >> 1

        return s
