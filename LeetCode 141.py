class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        processed = set()
        cur = head
        while cur:
            if cur in processed:
                return True
            else:
                processed.add(cur)
            cur = cur.next
        return False


    def hasCycle_2(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False