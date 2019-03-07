class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def miniDepth(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.miniDepth(root.left), self.miniDepth(root.right)) + 1
        else:
            return max(self.miniDepth(root.left), self.miniDepth(root.right)) + 1