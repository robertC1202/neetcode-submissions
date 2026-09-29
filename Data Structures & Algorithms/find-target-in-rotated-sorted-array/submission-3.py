class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_index = l

        #Array is the original ascending order array
        if min_index == 0:
            l = 0
            r = len(nums) - 1

        # Target is on the left sorted portion of the array
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l = 0
            r = min_index - 1
        
        # Target is in the right sorted portion of the array
        else:
            l = min_index
            r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1