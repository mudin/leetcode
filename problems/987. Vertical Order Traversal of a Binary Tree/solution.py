# Definition for a binary tree node.
# 987. Vertical Order Traversal of a Binary Tree

from collections import defaultdict
from bisect import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root):
        dic = defaultdict(lambda: defaultdict(list))

        def dfs(t, x, y):
            if not t:
                return

            bisect.insort(dic[x][y], t.val)

            dfs(t.left, x - 1, y + 1)
            dfs(t.right, x + 1, y + 1)

        dfs(root, 0, 0)

        res = []
        xx = sorted(list(dic.keys()))

        for x in xx:
            arr = []
            yy = sorted(list(dic[x].keys()))
            for y in yy:
                arr += dic[x][y]
            res.append(arr)

        return res
