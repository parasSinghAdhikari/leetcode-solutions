class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        tempi=head
        tempj= head.next
        prev=head.val
        while tempj!=None:
            if tempj.val!= prev:
                tempi=tempi.next
                tempi.val=tempj.val
            prev = tempj.val
            tempj=tempj.next 
        tempi.next = None
        return head