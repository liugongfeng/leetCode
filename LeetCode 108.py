class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :param nums: List[int]
        :return: TreeNode
        """
        def toBST(nums, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = toBST(nums, start, mid - 1)
            node.right = toBST(nums, mid + 1, end)
            return node

        return toBST(nums, 0, len(nums) - 1)




