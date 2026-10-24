# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0

        def dfs(root_copy):
            if not root_copy:
                return 0
            
            left = dfs(root_copy.left)
            right = dfs(root_copy.right)
            
            self.result = max(self.result, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.result



        



        
        