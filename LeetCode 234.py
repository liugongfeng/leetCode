class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next

        if fast:
            slow = slow.next
        
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True