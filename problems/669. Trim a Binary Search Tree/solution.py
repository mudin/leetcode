# 669. Trim a Binary Search Tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root, low, high):
        def dfs(t):
            if not t:
                return None

            if t.val < low:
                return dfs(t.right)

            if t.val > high:
                return dfs(t.left)

            t.left = dfs(t.left)
            t.right = dfs(t.right)
            return t

        return dfs(root)
