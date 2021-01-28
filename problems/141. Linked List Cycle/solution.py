# 141. Linked List Cycle
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if not head:
            return False

        slow = head
        fast = slow.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
