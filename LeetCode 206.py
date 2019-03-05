class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next , prev, cur = prev, cur, cur.next
        return prev


"""  1 2 3 4 5 null
     5 4 3 2 1 null
 """