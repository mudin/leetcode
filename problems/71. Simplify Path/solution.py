# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path):
        path = path.split('/')
        stack = []
        for ch in path:
            if not ch or ch == '.':
                continue

            if ch == '..':
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(ch)

        return '/' + "/".join(stack)
