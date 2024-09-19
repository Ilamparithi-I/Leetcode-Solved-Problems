# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodeMax(root, -100000)
    
    # Root with maximum value of the path before it
    def goodNodeMax(self, root, maxi):
        if root==None:
            return 0
        if root.val >= maxi:
            return 1 + self.goodNodeMax(root.left, root.val) + self.goodNodeMax(root.right, root.val)
        else:
            return self.goodNodeMax(root.left, maxi) + self.goodNodeMax(root.right, maxi)
        
# Or

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxi=-100000) -> int:
        if root==None:
            return 0
        if root.val >= maxi:
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
        else:
            return self.goodNodes(root.left, maxi) + self.goodNodes(root.right, maxi)