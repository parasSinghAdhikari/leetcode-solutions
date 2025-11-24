class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root:TreeNode) -> int:
        sums = -2**32-1
        def maxpath(node):
            nonlocal sums
            if node==None:
                return 0
            left= max(maxpath(node.left),0)
            right =max(maxpath(node.right),0)
            
            sums = max(sums,left+right+node.val)
            return max(left+node.val,right+node.val)
        
        maxpath(root)
        
        return sums
        