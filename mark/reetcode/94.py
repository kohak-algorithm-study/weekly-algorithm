from typing import List


class Solution:
    def inorderTraversal(self, root) -> List[int]:

        nodes = []

        # 각 루트 값에 대해 TreeNode 객체를 생성하여 리스트에 추가
        for i in range(len(root)):
            nodes.append(TreeNode(root[i]))

        print(nodes)

        return nodes


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None



root = [1, None, 2, 3]
Solution().inorderTraversal(root=root)