# 31. Next Permutation


class Solution:
    def nextPermutation(self, A):
        n = len(A)
        i = n - 2
        while i >= 0 and A[i + 1] <= A[i]:
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0 and A[j] <= A[i]:
                j -= 1
            A[i], A[j] = A[j], A[i]

        l, r = i + 1, n - 1
        while l < r:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1
