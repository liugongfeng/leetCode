class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        pos = root
        parent = None
        while pos is not None:
            parent = pos
            if val < pos.val:
                pos = pos.left
            else:
                pos = pos.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root