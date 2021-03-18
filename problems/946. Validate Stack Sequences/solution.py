# 946. Validate Stack Sequences
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        i, stack = 0, []
        for x in pushed:
            stack.append(x)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return i == len(popped)

    def validateStackSequences(self, pushed, popped):
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0
