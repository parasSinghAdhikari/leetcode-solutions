### time complexity O(n) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        temp = []
        while head != None:
            temp.append(head.val)
            head=head.next
        num = 0
        p = 0
        for i in range(len(temp)-1,-1,-1):
            num+=(temp[i]*(2**p))
            p+=1
        return num        
        