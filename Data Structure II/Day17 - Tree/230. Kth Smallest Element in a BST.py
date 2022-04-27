# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root):
            if root==None: return []
            return in_order(root.left)+[root.val]+in_order(root.right)
        return in_order(root)[k-1]