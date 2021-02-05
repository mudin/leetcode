# 594. Longest Harmonious Subsequenc
from collections import Counter


class Solution:
    def findLHS(self, nums):
        res, counter = 0, Counter(nums)
        for num, c in counter.items():
            if num + 1 in counter:
                res = max(res, counter[num + 1] + c)
        return res
