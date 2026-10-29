# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        helper_array = []

        def dfs(root_copy):
            if not root_copy:
                return
            
            dfs(root_copy.left)
            helper_array.append(root_copy.val)
            dfs(root_copy.right)
        dfs(root)
        return helper_array[k - 1]
        


        