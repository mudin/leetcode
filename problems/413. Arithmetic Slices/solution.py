# 413. Arithmetic Slices
class Solution:
    # Brute force
    def numberOfArithmeticSlices2(self, A):
        n, res = len(A), 0
        if n < 3:
            return 0
        for i in range(n - 2):
            dif = A[i + 1] - A[i]
            j = i + 2
            while j < n and A[j] - A[j - 1] == dif:
                j += 1
                res += 1
        return res

    # DP with O(1) space
    def numberOfArithmeticSlices(self, A):
        n, res, cur = len(A), 0, 0
        for i in range(1, n - 1):
            if A[i - 1] + A[i + 1] == 2 * A[i]:
                cur += 1
                res += cur
            else:
                cur = 0
        return res

    def numberOfArithmeticSlices(self, A):
        n, res, cur = len(A), 0, 0
        for i in range(1, n - 1):
            k = A[i - 1] + A[i + 1] == 2 * A[i]
            cur = cur * k + k
            res += cur
        return res
