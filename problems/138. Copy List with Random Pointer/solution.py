# 138. Copy List with Random Pointer
"""
# Definition for a Node.
"""
from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
  # O(n) time, O(n) space, two pass
  def copyRandomList1(self, head):
    
    cur, dc = head, {}
    
    while cur:
      dc[cur] = Node(cur.val)
      cur = cur.next
    
    cur = head
    
    while cur:
      dc[cur].next = dc.get(cur.next)
      dc[cur].random = dc.get(cur.random)
      cur = cur.next
    
    return dc.get(head)
    
  # O(n) time, O(n) space  one pass
  def copyRandomList2(self, head):
    dc = defaultdict(lambda: Node(0), {None:None})
    cur = head
    while cur:
      dc[cur].val = cur.val
      dc[cur].next = dc[cur.next]
      dc[cur].random = dc[cur.random]
      cur = cur.next
    return dc[head]
  
  # O(n) time, O(1) space  
  def copyRandomList(self, head):
    
    # First round: make copy of each node,
    # and link them together side-by-side in a single list.
    cur = head
    while cur:
      nxt = cur.next
      copy = Node(cur.val)
      cur.next = copy
      copy.next = nxt
      cur = nxt

    # Second round: assign random pointers for the copy nodes.
    cur = head
    while cur:
      if cur.random:
        cur.next.random = cur.random.next
      cur = cur.next.next

    # Third round: restore the original list, and extract the copy list.
    cur, res = head, Node(0)
    p = res

    while cur:
      nxt = cur.next.next;

      # extract the copy
      copy = cur.next
      p.next = copy
      p = copy

      # restore the original list
      cur.next = nxt
      cur = nxt

    return res.next
        