# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = ListNode(-1000)
        l.next = head
        for i in range(left-1):
            l = l.next
        r =l.next
        temp = None
        for j in range(right-left+1):
            nexts = r.next
            r.next= temp
            temp =r 
            r = nexts
        l.next.next = r
        l.next = temp

        if left >1:
            return head
        return l.next
            
        

        
        