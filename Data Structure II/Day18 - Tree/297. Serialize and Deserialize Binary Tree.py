# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        s=''
        q=deque([root])
        while q:
            node=q.popleft()
            if node:
                s+=str(node.val)+' '
                q.append(node.left)
                q.append(node.right)
            else:
                s+='n '
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        values=data.split()
        root=TreeNode(values[0])
        q=deque([root])
        for i in range(1, len(values), 2):
            node=q.popleft()
            if values[i]!='n':
                node.left=TreeNode(values[i])
                q.append(node.left)
            if values[i+1]!='n':
                node.right=TreeNode(values[i+1])
                q.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))