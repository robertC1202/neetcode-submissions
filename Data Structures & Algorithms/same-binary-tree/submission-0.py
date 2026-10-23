# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(tree_p, tree_q):
            if not tree_p and not tree_q:
                return True
            
            if not tree_p or not tree_q or tree_p.val != tree_q.val:
                return False
            

            return (dfs(tree_p.left, tree_q.left) and dfs(tree_p.right, tree_q.right))
        
        return dfs(p, q)
