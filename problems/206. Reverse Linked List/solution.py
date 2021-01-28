# 206. Reverse Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList2(self, head):
        prev, cur = None, head
        while cur:
            prev = ListNode(cur.val, prev)
            cur = cur.next
        return prev
