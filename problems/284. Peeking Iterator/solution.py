# 284. Peeking Iterator

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.cur = self.getNextOrNone()

    def peek(self):
        return self.cur

    def next(self):
        cur = self.cur
        self.cur = self.getNextOrNone()
        return cur

    def hasNext(self):
        return self.cur != None

    def getNextOrNone(self):
        if self.iter.hasNext():
            return self.iter.next()
        return None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
