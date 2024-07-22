from typing import List


class Solution:
    def inorderTraversal(self, root) -> List[int]:
        output = []

        def dfs(node):
            if node:
                dfs(node.left)
                output.append(node.val)
                dfs(node.right)

        dfs(root)
        return  output

root = [1, None, 2, 3]
Solution().inorderTraversal()