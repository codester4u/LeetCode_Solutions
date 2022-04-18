# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        start=head
        while start:
            l+=1
            start=start.next
        left, right = 0, l//2
        while head:
            if left==right:
                return head
            else:
                left+=1
                head=head.next
        return False
        