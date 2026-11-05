# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, rootVal):
            if not root:
                return 0
            
            result = 1 if root.val >= rootVal else 0
            rootVal = max(rootVal, root.val)
            result += dfs(root.left, rootVal)
            result += dfs(root.right, rootVal)
            return result
        return dfs(root, root.val)
        
        


       
            