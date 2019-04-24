class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Stack  中序遍历
    def inorderTraversal(self, root:TreeNode) -> list[int]:
        result, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result


    # Recursive  中序遍历
    def method2(self, root:TreeNode) -> list[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root: TreeNode, result: list[int]):
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)




