# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        cur=dummy
        
        while cur.next and cur.next.next:
            temp1=cur.next
            temp2=cur.next.next
            
            #swapping
            cur.next, temp2.next, temp1.next = temp2, temp1, temp2.next
            cur=temp1
        return dummy.next