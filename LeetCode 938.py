class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0
        if L <= root.val <= R:
            result += root.val
        
        if root.val > L and root.left is not None:
            result += self.rangeSumBST(root.left, L, R)
        if root.val < R and root.right is not None:
            result += self.rangeSumBST(root.right, L, R)

        return result


    def method2(self, root: TreeNode, L:int, R:int)->int:
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    result += node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return result