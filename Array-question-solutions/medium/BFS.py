# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None :
            return []
        q = []
        ans= []
        q.append(root)
        while len(q)!=0:
            temp = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
                temp.append(node.val)
            ans.append(temp)
        return ans