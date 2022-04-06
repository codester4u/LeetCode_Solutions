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
        mid=l//2
        c=0
        while head:
            if c==mid:
                return head
            else:
                c+=1
                head=head.next
        return False
        