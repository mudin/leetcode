# 242. Valid Anagram
from collections import defaultdict, Counter


class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        d = defaultdict(int)

        for ch in s:
            d[ch] += 1

        for ch in t:
            d[ch] -= 1

        for c in d.values():
            if c != 0:
                return False

        return True
