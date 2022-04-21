# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited=set()
        curA, curB = headA, headB
        while curA:
            visited.add(curA)
            curA=curA.next
        while curB:
            if curB in visited:
                return curB
            curB=curB.next
        return None


