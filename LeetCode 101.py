class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :param root: TreeNode
        :return:     bool
        """
        if root is None:
            return True
        return self.Helper(root.left, root.right)


    def Helper(self, left, right):
        """
        :param left:  TreeNode
        :param right:   TreeNode
        :return:   Bool
        """
        if left is None and right is None:
            return True
        if left is not None or right is not None or left.val != right.val:
            return False

        return self.Helper(left.left, right.right) and self.Helper(left.right, right.left)








