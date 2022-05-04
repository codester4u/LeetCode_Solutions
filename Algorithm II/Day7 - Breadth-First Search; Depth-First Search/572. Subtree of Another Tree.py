class Solution:
    def isSubtree(self, root, subRoot):
        if not root: return False
        if(self.sameTree(root, subRoot)): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def sameTree(self, root, subRoot):
        if not root or not subRoot: return root==subRoot
        return root.val==subRoot.val and self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)