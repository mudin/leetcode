# 11. Container With Most Water

class Solution:
    def maxArea(self, arr):
        l, r = 0, len(arr) - 1
        res = 0

        while l < r:

            if arr[l] > arr[r]:
                res = max(res, arr[r] * (r - l))
                r -= 1
            else:
                res = max(res, arr[l] * (r - l))
                l += 1

        return res
