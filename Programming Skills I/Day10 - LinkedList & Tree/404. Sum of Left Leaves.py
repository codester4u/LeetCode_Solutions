# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.su=0
        def sumofLeaves(root,isLeft):
            if isLeft and root.left==None and root.right==None:
                self.su+=root.val
                return
            else:
                if root.left!=None: sumofLeaves(root.left,True)
                if root.right!=None: sumofLeaves(root.right,False)
        if root==None: return 0
        sumofLeaves(root,False)
        return self.su