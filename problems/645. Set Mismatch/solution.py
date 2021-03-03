# 645. Set Mismatch
from collections import Counter


class Solution:
    def findErrorNums2(self, nums):
        counter = Counter(nums)
        n, res = len(nums), []
        for i in range(1, n + 1):
            if not counter.get(i):
                res.append(i)
            elif counter.get(i) == 2:
                res.insert(0, i)
        return res

    def findErrorNums(self, nums):
        n = len(nums)
        s = n*(n+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]
