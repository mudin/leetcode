# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode1(self, A, B):
        a, n = A, 0
        while a:
            a = a.next
            n += 1

        b, m = B, 0
        while b:
            b = b.next
            m += 1

        a, b = A, B

        if n > m:
            for i in range(n - m):
                a = a.next

        if m > n:
            for i in range(m - n):
                b = b.next

        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next

        return None

    def getIntersectionNode(self, A, B):

        if not A or not B:
            return None

        a, b = A, B

        while a != b:
            a = B if not a else a.next
            b = A if not b else b.next

        return a
