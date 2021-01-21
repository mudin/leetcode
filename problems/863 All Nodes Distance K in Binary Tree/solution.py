# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        res = []

        def find(t, k):
            if not t:
                return
            if k == 0:
                res.append(t.val)

            find(t.left, k - 1)
            find(t.right, k - 1)

        def dfs(t):
            if not t:
                return [False, 0]

            if t == target:
                find(t, K)
                return [True, K - 1]

            left = dfs(t.left)
            right = dfs(t.right)

            if left[0]:
                if left[1] == 0:
                    res.append(t.val)
                elif left[1] > 0:
                    find(t.right, left[1] - 1)
                    return [True, left[1] - 1]
            if right[0]:
                if right[1] == 0:
                    res.append(t.val)
                elif right[1] > 0:
                    find(t.left, right[1] - 1)
                    return [True, right[1] - 1]
            return [False, 0]

        dfs(root)

        return res
