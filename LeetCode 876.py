class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = head
        while dummy and dummy.next:
            head = head.next
            dummy = dummy.next.next

        return head