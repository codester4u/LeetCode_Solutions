# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirrot(root,root)
    def mirrot(self,s,b):
        if s==None and b==None: return True
        if s==None or b==None: return False
        return s.val==b.val and self.mirrot(s.right,b.left) and self.mirrot(b.right, s.left)
        
        