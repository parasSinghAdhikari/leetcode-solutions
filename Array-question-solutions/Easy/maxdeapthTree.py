# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def backtrack(node,i):
            nonlocal maxi
            if node==None:
                maxi = max(i,maxi)
                return
            ans = i+1 
            backtrack(node.left,ans)
            ans=i+1
            backtrack(node.right,ans)
        backtrack(root,0)
        return maxi
        