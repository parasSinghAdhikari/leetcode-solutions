from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n= len(lists)       
        if n==0:
            return None
        while len(lists)>1:
            if lists[0]==None:
                lists.pop(0)
                continue
            if lists[1]==None:
                lists.pop(1)
                continue
            if lists[0].val<=lists[1].val:
                root  = lists[0] 
                temp1 = root.next
                temp2 = lists[1] 
            else:
                root  = lists[1]
                temp1 = lists[0]
                temp2 = root.next 
            temp3= root
            while temp1!=None and temp2!=None:
                if temp1.val<=temp2.val:
                    node = ListNode(temp1.val)
                    temp3.next = node
                    temp1 =temp1.next
                else:
                    node = ListNode(temp2.val)
                    temp3.next = node
                    temp2 =temp2.next
                temp3= temp3.next
            if temp1!=None:
                temp3.next = temp1
            if temp2!=None:
                temp3.next = temp2
            lists.pop(0)
            lists.pop(0)
            lists.append(root)
        return lists[0]    
            
            
                
            
        