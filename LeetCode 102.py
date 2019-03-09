import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.result         # for DFS


class Solution:
    # BFS
    def levelOrder(self, root):
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        result = []

        # visited = set()

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result



    # DFS
    def levelOrder_2(self, root):
        if not root:
            return []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return

        if len(self.result) < level:
            self.result.append([])

        self.result[level].append(node.val)
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


        # if not node:
        #     return
        # if len(self.result) < level + 1:
        #     self.result.append([])
        # self.result[level].append(node.val)
        #
        # self._dfs(node.left, level + 1)
        # self._dfs(node.right, level + 1)