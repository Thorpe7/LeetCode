from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []
        self.inorder(root, inorder_list)
        return inorder_list


    def inorder(self,node:Optional[TreeNode], inorder_list: List[int]):
        if not node:
            return

        self.inorder(node.left, inorder_list)
        inorder_list.append(node.val)
        self.inorder(node.right, inorder_list)
