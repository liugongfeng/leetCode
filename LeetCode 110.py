class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :param root: TreeNode
        :return:   bool
        """
        def getHeight(root):
            if root is None:
                return 0
            left, right = getHeight(root.left), getHeight(root.right)

            if left < 0 or right < 0 or abs(left - right):
                return -1

            return max(left, right) + 1
        return  getHeight(root) >= 0
