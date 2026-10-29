# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validateBST(root_copy, lower_bound, upper_bound):
            if not root_copy:
                return True
            
            if not lower_bound < root_copy.val < upper_bound:
                return False
            
            left = validateBST(root_copy.left, lower_bound, root_copy.val)
            right = validateBST(root_copy.right, root_copy.val, upper_bound)

            return left and right


        return validateBST(root, -float("inf"), float("inf")) 


       
        