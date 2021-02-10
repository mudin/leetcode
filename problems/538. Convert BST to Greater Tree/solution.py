# 538. Convert BST to Greater Tree
class Solution:
    # with global variable
    def convertBST(self, root):
        s = 0

        def dfs(t):
            if not t:
                return
            nonlocal s

            dfs(t.right)
            s = t.val = s + t.val
            dfs(t.left)

        dfs(root)
        return root

    # without global variable
    def convertBST2(self, root):
        def dfs(t, val):
            if not t:
                return val

            right = dfs(t.right, val)
            t.val += right
            left = dfs(t.left, t.val)

            return left

        dfs(root, 0)

        return root
