# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    #  reverse all
    def isPalindrome1(self, head):
        prev, cur = None, head
        while cur:
            prev = ListNode(cur.val, prev)
            cur = cur.next

        # print(head, prev)

        while head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True

    #  2 runners, reverse half
    def isPalindrome(self, head):

        def reverseList(head):
            prev, cur = None, head
            while cur:
                prev = ListNode(cur.val, prev)
                cur = cur.next
            return prev

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        slow = reverseList(slow)
        fast = head

        while slow:
            if fast.val != slow.val:
                return False

            fast = fast.next
            slow = slow.next

        return True
