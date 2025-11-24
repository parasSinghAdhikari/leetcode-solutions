# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head 
        temp =head.next 
        prev = None
        while head!=None and head.next!=None:
            node = head.next
            head.next = head.next.next
            node.next = head
            if prev==None:
                prev=head
            else:
                prev.next=node
                prev=head
            head = head.next

        return temp
            
