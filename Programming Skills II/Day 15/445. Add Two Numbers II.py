# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 =0, 0
        while l1:
            num1=num1*10+l1.val
            l1=l1.next
        while l2:
            num2=num2*10+l2.val
            l2=l2.next
        su=num1+num2
        cur=head=ListNode(0)
        
        if su==0: return head
        while su>0:
            head.next=ListNode(su%10)
            head=head.next
            su//=10
            
        prev=None
        head=cur.next
        while head:
            nxt=head.next
            head.next=prev
            prev=head
            head=nxt
        return prev