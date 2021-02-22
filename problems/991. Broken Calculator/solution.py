# 991. Broken Calculator
class Solution:
    def brokenCalc(self, x, y):
        res = 0
        while x < y:
            if y % 2:
                y += 1
            else:
                y //= 2
            res += 1
        return res + x - y
