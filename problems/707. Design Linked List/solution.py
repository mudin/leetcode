# 707. Design Linked List
# https://leetcode.com/problems/design-linked-list/


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        cur = self.head
        while cur and index:
            index -= 1
            cur = cur.next

        return cur.val

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        self.size += 1

        if not self.head:
            self.head = ListNode(val)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        self.size += 1

        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head

        while cur and index > 1:
            index -= 1
            cur = cur.next

        node = ListNode(val)
        node.next = cur.next
        cur.next = node

        # self.printArray()

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        cur = self.head
        if index == 0:
            self.head = cur.next
            return

        while cur and index > 1:
            index -= 1
            cur = cur.next

        cur.next = cur.next.next

    def printArray(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
