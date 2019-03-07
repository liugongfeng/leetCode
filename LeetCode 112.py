class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :param root: TreeNode
        :param sum:  int
        :return:     bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)