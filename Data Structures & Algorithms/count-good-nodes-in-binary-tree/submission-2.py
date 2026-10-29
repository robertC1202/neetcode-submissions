# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(root_copy, val):
            if not root_copy:
                return 0

            res = 1 if root_copy.val >= val else 0
            val = max(val, root_copy.val)
            res += dfs(root_copy.left,val)
            res += dfs(root_copy.right,val)
            return res
        return dfs(root, root.val)
    


       
            