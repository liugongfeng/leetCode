class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        root.left = self.lowestCommonAncestor(root.left, p, q)
        root.right = self.lowestCommonAncestor(root.right, p, q)
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if root.left and root.right:
            return root
        