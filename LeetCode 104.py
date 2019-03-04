class TreeNode:
    def __index__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :param root: TreeNode
        :return:  int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1








