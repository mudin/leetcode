# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    #  BFS O(k) time, O(1) memory
    def rightSideView(self, root):
        if not root:
            return []

        q, res = [root], []
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                t = q.pop(0)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

        return res

    #  DFS O(k) time, O(h) memory
    def rightSideView2(self, root):
        d = {}

        def dfs(t, level):
            if not t:
                return

            d[level] = t.val
            dfs(t.left, level + 1)
            dfs(t.right, level + 1)

        dfs(root, 1)

        return d.values()
