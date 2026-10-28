# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.result = 0
        def dfs(root_copy, max_val):
            if not root_copy:
                return

            if root_copy.val >= max_val:
                self.result += 1
            new_max = max(max_val, root_copy.val)
            
            if root_copy.left:
                dfs(root_copy.left, new_max)
            if root_copy.right:
                dfs(root_copy.right, new_max)

            return self.result


        return dfs(root, root.val)