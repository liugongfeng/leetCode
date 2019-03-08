class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        self.prev = None
        return self.Helper(root)

    def Helper(self, root):
        if root is None:
            return True
        if not self.Helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.Helper(root.right)
