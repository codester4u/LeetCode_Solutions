# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root, sum_tot, lst, res):
        if root.left is None and root.right is None:
            if root.val == sum_tot:
                res+=[lst+[root.val]]
        if root.left: self.helper(root.left, sum_tot-root.val, lst+[root.val], res)
        if root.right: self.helper(root.right, sum_tot-root.val, lst+[root.val], res)
        return res
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root, targetSum, [], [])