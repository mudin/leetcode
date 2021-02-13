# 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num):
        i = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            i += 1
        return i

    def numberOfSteps(self, n):
        # digits = f'{n:b}'
        digits = "{0:b}".format(n)
        return digits.count('1') - 1 + len(digits)

    def numberOfSteps(self, n):
        if not n:
            return 0
        res = 0
        while n:
            res += 2 if n & 1 else 1
            n >>= 1
        return res - 1
