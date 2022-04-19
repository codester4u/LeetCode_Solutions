"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l=defaultdict(list)
        def dfs(root, level):
            if not root: return
            l[level].append(root.val)
            for i in root.children:
                dfs(i,level+1)
        dfs(root,0)
        return [lst for i, lst in sorted(l.items())]