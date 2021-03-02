# 581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray(self, nums):
        n, l, r = len(nums), -1, -2
        lmax, rmin = nums[0], nums[-1]
        for i in range(1, n):
            if lmax > nums[i]:
                r = i
            else:
                lmax = nums[i]

            if rmin < nums[n - i - 1]:
                l = n - i - 1
            else:
                rmin = nums[n - i - 1]

        return r - l + 1
