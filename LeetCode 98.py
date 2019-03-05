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
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, mini, maxi):
        if not root:
            return True
        if root.val >= maxi or root.val <= mini:
            return False
        return self.valid(root.left, mini, root.val) and self.valid(root.right, root.val, maxi)

    