class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, first: list[int], mid: list[int]) -> TreeNode:
        if not first or not mid:
            return None
        
        pivot = mid.index(first[0])
        left , right = mid[:pivot] , mid[pivot+1:]
        root = TreeNode(first[0])
        root.left = self.buildTree(first[1:len(left)+1], left)
        root.right = self.buildTree(first[-len(right):], right)
        
        return root