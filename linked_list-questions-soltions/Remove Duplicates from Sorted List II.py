# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempi =ListNode(0,head)
        tempj= tempi
        while head != None:
            if head.next and head.val==head.next.val:
                val = head.val
                while head!=None and head.val==val:
                    head =head.next
                tempj.next = head
            else:
                tempj= tempj.next
                head =head.next
        return tempi.next
        