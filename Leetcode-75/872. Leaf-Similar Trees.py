# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = self.listCreator(root1)
        list2 = self.listCreator(root2)
        if (list1 == list2):
            return True
        else:
            return False

    def listCreator(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        else:
            return self.listCreator(root.left) + self.listCreator(root.right)
        