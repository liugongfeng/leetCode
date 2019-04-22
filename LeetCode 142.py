class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        processed = set()
        cur = head
        while cur:
            if cur in processed:
                return cur
            else:
                processed.add(cur)
            cur = cur.next
        return None

    def method2(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast:
            if fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                find = head
                while find != slow:
                    find = find.next
                    slow = slow.next
                return find


