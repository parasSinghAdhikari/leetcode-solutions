# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = ListNode(-1000)
        b = ListNode(-1000)
        after = a
        before = b
        curr =head
        while curr!=None:
            if curr.val<x:
                b.next = curr
                b = b.next
            else:
                a.next = curr
                a = a.next
            curr = curr.next
        
        a.next = None         
        b.next = after.next

        return before.next 
        