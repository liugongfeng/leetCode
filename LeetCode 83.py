class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        current = head
        while current:
            runner = current.next
            while runner and runner.val == current.val:
                runner = runner.next

            current.next = runner
            current = runner

        return head


