# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_value=''
        while head:
            binary_value+=str(head.val)
            head=head.next
        return int(binary_value,2)
        